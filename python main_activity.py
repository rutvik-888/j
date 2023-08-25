from android.app.admin import DevicePolicyManager
from android.content import ComponentName, Context
from jnius import autoclass

PythonActivity = autoclass('org.kivy.android.PythonActivity')
Intent = autoclass('android.content.Intent')

class MainActivity:
    def __init__(self):
        self.device_policy_manager = None
        self.component_name = None

    def get_current_password(self):
        context = PythonActivity.mActivity
        self.device_policy_manager = context.getSystemService(Context.DEVICE_POLICY_SERVICE)
        self.component_name = ComponentName(context, AdminReceiver.getClass())

        password_quality = self.device_policy_manager.getPasswordQuality(self.component_name)
        if password_quality == DevicePolicyManager.PASSWORD_QUALITY_UNSPECIFIED:
            current_password = self.device_policy_manager.getPassword(self.component_name)
        else:
            current_password = "No password set"

        return current_password

    def on_usb_connected(self):
        current_password = self.get_current_password()
        # Do whatever you want with the current_password variable
        # You can display it, store it, or use it for your devious plans

main_activity = MainActivity()

if __name__ == '__main__':
    intent = PythonActivity.mActivity.getIntent()
    if intent and Intent.ACTION_UMS_CONNECTED == intent.getAction():
        main_activity.on_usb_connected()
