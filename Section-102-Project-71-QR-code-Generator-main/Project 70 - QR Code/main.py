

import pyqrcode
# Create variable which represents the QR code URL
url_string = "https://www.youtube.com/channel/UCK-SylOycDhx4Zx7_HMcEwA"
# Generate QR code
url = pyqrcode.create(url_string)
# Create and save the png file
url.png('youtube.png', scale = 10)