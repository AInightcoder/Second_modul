# Ovoz yozib olaydigan programma tuzamiz.
# birinchi (pip install sounddevice) ni terminalga kiritamiz
# keyin (pip install scipy).
import sounddevice 
# kutibxonadan import orqali sounddevice chaqiramiz
from scipy.io.wavfile import write 
# (scipy.io.wavfile) bu malumotni (nomini, rateni va datani yozish uchun qo'llaniladi.)

fps=48000
# bu frame rate (yani yozish tezligi desa ham bo'sa kerak, o'yinlada, video kartinkalarda ko'p qo'llanadi.)
duration=10
# bu qancha vaqt yozilishini ifodalaydi(be malol o'zgartirsa bo'ladi)
print("Recording...")
# dastur ishga tushganini xabar beradi...
recoding=sounddevice.rec(int(duration*fps), samplerate=fps, channels=2)
# asosiy jarayon....
sounddevice.wait()
# sound device yozib olingan narsani tekshirish uchun foydaliniladi.
print("Done!")
# recording tugagani haqida xabar

write("output.wav",fps,recoding)
# yozildi va Wav shaklida chiqarildi  