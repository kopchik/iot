import micropython

from .pcd8544 import PCD8544_FRAMEBUF


class LCD(PCD8544_FRAMEBUF):
    def __init__(self, *args, flipped=False, echo=False, **kwargs):
        super().__init__(*args, **kwargs)

        self._flipped = flipped
        self._echo = echo

    def log(self, t):
        if self._echo:
            print(t)
        self.scroll(0, -10)
        # prevent ghosting of prev image
        self.fill_rect(0, 40, 84, 10, 0)
        self.text(t, 0, 40, 1)
        self.show()

    def show(self):
        if not self._flipped:
            return super().show()

        lcd_data = self.buf
        lcd_data = self._flipped()
        self.data(lcd_data)

    @micropython.viper
    def _flipped(self):
        _buf = bytearray((48 // 8) * 84)
        inbuf = ptr8(self.buf)
        outbuf = ptr8(_buf)

        # https://stackoverflow.com/a/30002555
        for i in range(504):
            a = inbuf[i]
            a = (
                ((a & 0x1) << 7)
                | ((a & 0x2) << 5)
                | ((a & 0x4) << 3)
                | ((a & 0x8) << 1)
                | ((a & 0x10) >> 1)
                | ((a & 0x20) >> 3)
                | ((a & 0x40) >> 5)
                | ((a & 0x80) >> 7)
            )
            outbuf[503 - i] = a
        return _buf
