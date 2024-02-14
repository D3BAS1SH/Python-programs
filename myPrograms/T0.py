from urllib.parse import unquote
import base64
""" 
decode0=base64.b64decode('3313b0b73f9482adc36cdef8e86bb754').decode('utf-8') """

decoded0=unquote('32d49278f28c78229de164fe79dc13b6adb3c98af2d133240eb1ffc44771ad3da%3A2%3A%7Bi%3A0%3Bs%3A8%3A%22language%22%3Bi%3A1%3Bs%3A2%3A%22en%22%3B%7D	')
decoded1=unquote('3313b0b73f9482adc36cdef8e86bb754')
decoded2=unquote('3313b0b73f9482adc36cdef8e86bb754')
print(decoded0)
""" print(decoded1)
print(decoded2) """