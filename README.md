# Površinska napetost

## Metoda viseće kapljice

**Inin laboratorij**

U komoru uređaja ispunjenog jednim fluidom koji može biti pri atmosferskom ili pri povišenom tlaku se utiskuje kroz kapilarnu cijev uzorak nafte.
Uzorak nafte poprima oblik kapljice. Zatim se fotografira taj isti uzorak s određene udaljenosti. 

### Slika kapljice
![kap2](https://user-images.githubusercontent.com/59419133/145826370-8ea89d5c-d15e-4a35-93bf-e0e5e3ebed1b.jpg)

Kako bi dobili kapljice trebamo prije obraditi sliku sljedećim funkcijama:

```python
kap_gray = cv2.cvtColor(kap, cv2.COLOR_BGR2GRAY)
kap_smooth = cv2.GaussianBlur(kap_gray, (3, 3), 2, 2)

kap_canny = cv2.Canny(kap_smooth, 128, 255)
kap_canny = cv2.dilate(kap_canny, None, iterations=1)
kap_canny = cv2.erode(kap_canny, None, iterations=1)
```

Kako bi dobili trazenu konturu koristimo iducu funkciju:

```
trazenaKontura = np.zeros(kap_canny.shape, np.uint8)
```

### Slika konture kapljice
![kap konture](https://user-images.githubusercontent.com/59419133/145827383-e715d378-d1ae-4cba-832b-a24987e1a8ff.jpg)

Zatim brojanjem piksela i sa zadanim promjerom kapilare koja se koristi kao mjerilo možemo izračunati tražene promjere kapljice.

### Traženi promjeri kapljice
![image](https://user-images.githubusercontent.com/59419133/145827976-5a69da41-5b52-4e7a-bc8e-a5e65d6617b1.png)

Pomoću korekcijskih faktora iz excel tablice H.xlxs računamo konačnu vrijednost površinske napetosti uzorka nafte.

