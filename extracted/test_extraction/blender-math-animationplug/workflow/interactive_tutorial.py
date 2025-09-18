import bpy

class InteractiveTutorial(bpy.types.PropertyGroup):
    """交互式教程，引导用户完成基本操作"""
    
    _steps = []
    _current_step = 0

    def start(self):
        """开始教程"""
        self._steps = [
            self._step_1_intro,
            self._step_2_create_object,
            self._step_3_animate,
            self._step_4_render,
            self._step_5_finish
        ]
        self._current_step = 0
        self.next_step()

    def next_step(self):
        """进行到教程的下一步"""
        if self._current_step < len(self._steps):
            step_func = self._steps[self._current_step]
            step_func()
            self._current_step += 1
        else:
            self.finish()

    def finish(self):
        """结束教程"""
        bpy.context.window_manager.popup_menu(
            lambda self, context: self.layout.label(text="教程已完成!"), 
            title="教程结束", 
            icon='INFO'
        )

    def _show_message(self, title, message, icon='INFO'):
        def draw(self, context):
            self.layout.label(text=message)
            self.layout.operator("math_anim.tutorial_next_step", text="下一步")
        bpy.context.window_manager.popup_menu(draw, title=title, icon=icon)

    # --- 教程步骤定义 ---

    def _step_1_intro(self):
        self._show_message("欢迎!", "欢迎使用数学动画插件教程。我们将引导您完成基本操作。")

    def _step_2_create_object(self):
        self._show_message("第一步: 创建对象", "请转到'创建数学对象'面板，然后点击'添加2D曲线'。")
        # (可以在这里添加代码来高亮UI元素)

    def _step_3_animate(self):
        self._show_message("第二步: 添加动画", "选择您创建的曲线，然后转到'动画系统'面板，应用一个'路径绘制'动画。")

    def _step_4_render(self):
        self._show_message("第三步: 风格化", "现在，去'渲染与风格化'面板，尝试应用一个'白板'风格。")

    def _step_5_finish(self):
        self._show_message("恭喜!", "您已完成基本流程。探索更多功能吧！")