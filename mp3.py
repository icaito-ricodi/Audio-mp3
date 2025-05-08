from gtts import gTTS
import os

text = "Hola me llamo Ricardo, y tu como te llamas, rica. ¿Quién soy? Quimera de mi existir, realidad, mito o inconsciencia, había una vez un ser humano nacido en los años 70, fruto del amor de una pareja de escasos recursos, cuenta la historia que la realidad se confunde con lo inexplicable, al no tener el razonamiento suficiente y necesario no se alcanza a comprender las situaciones que suceden, en tu inconsciente sueño, todo se origina con la creación de la vida y de nuestro entorno, ya que al nacer en este bello país guadalupano, y el llegar a este universo después de librar una gran batalla entre miles de espermatozoides, ya eres un ganador, por el simple hecho de respirar y todos tenemos algo en común, ser Mexicanos y representar una raza humana semejante a nuestro padre. unidos en situaciones difíciles e incómodas, fui un niño en un espacio lleno de carencias pero a la vez con un amor incondicional de parte de mis seres queridos, recordando el ayer y en mis vagos recuerdos alcanzó a divagar que vivía en un espacio de unidad familiar, e imaginaba que era el único y más maravilloso mundo a mi alrededor, hoy estando en casa con una nueva familia, aún  recuerdo y añoro aquellos tiempos que no volverán, los primeros días de mi existir, mis primeros pasos con mis seres queridos y una infancia sin violencia, me hace reflexionar con la finalidad de gestionar la relación y los lazos que nunca se romperán, pienso a la gente más cercana de mi vida, así como en todos los ámbitos que me rodean, y hay ocasiones en que la locura me alcanza, pero solo es un sueño que supera lo cotidiano, sintiéndome atrapado entre dos vidas, también hay ocasiones que no quiero sumergirme en mis sueños pues tengo miedo, porque algunas veces me hacen sufrir sin saberlo, al recordar sucesos anteriores o imaginando cosas inexplicables, ¿Quién soy?, Ricardo es un nombre simple y común, una persona insignificante en un espacio infinito, pero a la vez un ser humano grande y bendecido por el creador, cuestionando en mi mente el paso por este mundo no alcanzo a comprender el porqué y para que ocupó un lugar en el universo, en realidad no encuentro el verdadero significado de mi existir, me pregunto qué es la vida, existir, un tiempo en el que pasamos por un ciclo sin poder comprender para qué fuimos creados y el propósito del ser supremo para con uno mismo, ya que el tiempo tarde o temprano nos alcanza, todo principio tiene un fin, mi mente a pesar de estar activa no alcanza a comprender mi existir, mi respirar, mi movimiento etc., en un mundo donde la hipocresía y la avaricia se ha apoderado de los seres pensantes, pero todo esto es una obra maestra de nuestro creador y debemos de ser agradecidos y ser bien portados, con el fin de alcanzar otro espacio en un lugar desconocido pero anhelado, muchas veces me pregunto cuál es mi destino y final, la incertidumbre de un futuro incierto me da pavor y me lleva a pensar tantas cosas sin alcanzar a comprender, el momento definitivo de mi existir, dejando atrás mucho y a la vez nada, por tal motivo te invito a reflexionar en tu existir en esta vida y no pases desapercibido como un (fantasma), a pesar de ser un humano, inteligente, pensante, no alcanzo a comprender mi existir en este espacio, que ocupó por algunos años, ya que en un abrir y cerrar de ojos sientes que se te acaba el soplo de vida, quién soy, qué hago, qué quiero, oh señor guía mis pasos, por favor te lo pido de corazón y dándote gracias por el tiempo que me has concedido en la tierra, quisiera dejar huella, pero soy una marioneta, una pieza moldeable por la mano de Dios y aunque todo a mi alrededor es algo cotidiano, a veces siento que soy un extraño en mi hábitat, hoy extraño mi infancia y la inocencia, pero el tiempo pasa y la gente cambia, por tal motivo vive y disfruta tu tiempo antes de dejar un vacío en el espacio, posdata, sólo siendo un genio o teniendo un don especial alcanzaría a comprender mi existir, Ricky DIOS, medio siglode existir, significado de existir, verbo intransitivo, 1., tener realidad física o mental, una persona o una cosa, las ideas existen en nuestra mente, 2., tener vida, un ser humano, mientras ellos existan, podrás sentirte protegido y acompañado."

language = "es-us"

speach = gTTS(text = text, lang = language, slow = False)

speach.save("texto.mp3")

os.system("start texto.mp3")

'''from gtts import gTTS
from playsound import playsound

text = "Hola me llamo Ricardo, y tu como te llamas, rica.  ¿Quién soy? Quimera de mi existir realidad, mito o inconsciencia."

s = gTTS("Sample Text")
s.save('sample.mp3')
playsound('sample.mp3')'''

'''import pyttsx3 

text = "Hola me llamo Ricardo, y tu como te llamas."

s = pyttsx3.init()  
data = "Sample Text"  
s.say(data)  
s.runAndWait()'''
input()