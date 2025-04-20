from onvif import ONVIFCamera

class OnvifClient:
    def __init__(self, host, port, user, password):
        self.host = host
        self.port = port
        self.user = user
        self.password = password
        self.cam = None

    def connect(self):
        try:
            self.cam = ONVIFCamera(self.host, self.port, self.user, self.password)
            return True, None
        except Exception as e:
            return False, str(e)

    def get_device_information(self):
        if not self.cam:
            raise RuntimeError("No ONVIF camera connected.")
        return self.cam.devicemgmt.GetDeviceInformation()
