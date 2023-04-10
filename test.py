from scipy.signal import get_window
from scipy.signal.windows import chebwin
window_length = 1024
attenuation = 60
window=get_window(('chebwin',attenuation),window_length)
print(window)
