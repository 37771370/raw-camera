import kivy
from kivy.app import App
from kivy.uix.boxlayout import BoxLayout
from kivy.uix.button import Button
from kivy.uix.slider import Slider
from kivy.uix.label import Label
from kivy.uix.camera import Camera
from kivy.core.window import Window
from kivy.graphics.texture import Texture
from kivy.clock import Clock
import cv2
import numpy as np
import os
from datetime import datetime
from kivy.utils import platform

kivy.require('2.0.0')

class RawCameraApp(App):
    def build(self):
        self.title = "原图直出相机"
        
        # 主布局
        main_layout = BoxLayout(orientation='vertical', padding=10, spacing=10)
        
        # 相机预览
        self.camera = Camera(play=True, resolution=(1920, 1080))
        main_layout.add_widget(self.camera)
        
        # 控制面板
        control_layout = BoxLayout(orientation='horizontal', size_hint_y=0.15, spacing=10)
        
        # 变焦滑块
        zoom_layout = BoxLayout(orientation='vertical', size_hint_x=0.7)
        zoom_label = Label(text='焦距调整: 1.0x', size_hint_y=0.3)
        self.zoom_slider = Slider(min=1.0, max=3.0, value=1.0, size_hint_y=0.7)
        self.zoom_slider.bind(value=self.on_zoom_change)
        zoom_layout.add_widget(zoom_label)
        zoom_layout.add_widget(self.zoom_slider)
        control_layout.add_widget(zoom_layout)
        
        # 拍照按钮
        photo_button = Button(text='拍照', size_hint_x=0.3, font_size=20)
        photo_button.bind(on_press=self.take_photo)
        control_layout.add_widget(photo_button)
        
        main_layout.add_widget(control_layout)
        
        # 状态标签
        self.status_label = Label(text='准备就绪', size_hint_y=0.05)
        main_layout.add_widget(self.status_label)
        
        # 变焦参数
        self.zoom_factor = 1.0
        self.zoom_label = zoom_label
        
        # 保存路径
        if platform == 'android':
            from android.storage import primary_external_storage_path
            self.save_path = os.path.join(primary_external_storage_path(), 'Pictures', 'RawCamera')
        else:
            self.save_path = os.path.join(os.path.expanduser('~'), 'Pictures', 'RawCamera')
        
        if not os.path.exists(self.save_path):
            os.makedirs(self.save_path)
        
        return main_layout
    
    def on_zoom_change(self, instance, value):
        self.zoom_factor = value
        self.zoom_label.text = f'焦距调整: {value:.1f}x'
    
    def take_photo(self, instance):
        try:
            # 获取相机帧
            texture = self.camera.texture
            if texture:
                # 将纹理转换为numpy数组
                pixels = texture.pixels
                arr = np.frombuffer(pixels, dtype=np.uint8)
                arr = arr.reshape(texture.height, texture.width, 4)
                
                # 转换BGR格式
                frame = cv2.cvtColor(arr, cv2.COLOR_RGBA2BGR)
                
                # 应用变焦
                if self.zoom_factor > 1.0:
                    frame = self.apply_zoom(frame)
                
                # 生成文件名
                timestamp = datetime.now().strftime("%Y%m%d_%H%M%S")
                filename = f"raw_photo_{timestamp}.jpg"
                filepath = os.path.join(self.save_path, filename)
                
                # 保存高质量JPG
                cv2.imwrite(filepath, frame, [cv2.IMWRITE_JPEG_QUALITY, 95])
                
                self.status_label.text = f'已保存: {filename}'
                print(f"照片已保存: {filepath}")
                
        except Exception as e:
            self.status_label.text = f'保存失败: {str(e)}'
            print(f"错误: {str(e)}")
    
    def apply_zoom(self, frame):
        height, width = frame.shape[:2]
        
        # 计算裁剪区域
        new_height = int(height / self.zoom_factor)
        new_width = int(width / self.zoom_factor)
        
        # 计算裁剪起始位置（居中裁剪）
        start_y = (height - new_height) // 2
        start_x = (width - new_width) // 2
        
        # 裁剪
        cropped = frame[start_y:start_y+new_height, start_x:start_x+new_width]
        
        # 缩放回原始尺寸
        zoomed = cv2.resize(cropped, (width, height), interpolation=cv2.INTER_LINEAR)
        
        return zoomed

if __name__ == '__main__':
    RawCameraApp().run()
