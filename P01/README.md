# El dogma central de la biología molecular
Práctica por: **Nayeli Luis**

## Características generales

1. <font color="red">Ésta práctica es para computólogos/as. Si eres biólgo/a envíame un correo.</font>

2. Práctica que se entrega en **parejas**. 

3. Entregables: 
  * Un archivo PDF con respuestas y descripción del programa. Este archivo debe contener los nombres de los integrantes del equipo y el formato de su nombre es el siguiente: `p1_ApellidoNombre_cuestionario.pdf`
  * Un script en `Python` (`.py`). Este archivo debe tener como comentario los nombres de los integrantes y el formato del nombre es: `p1_ApellidoNombre.py`.

Ambos archivos se entregan en Clasroom, y lo deben entregar los dos integrantes del equipo. 

## Instrucciones 

1. Revisen la siguiente [lista](https://docs.google.com/spreadsheets/d/1UKyPqcmmgYuCQQb5_Zoyt-pTuSA4itq7/edit?usp=share_link&ouid=117981748854039384449&rtpof=true&sd=true), elijan dos biomoléculas, una de la sección amarilla y otra de la sección azul.

2. Busquen los archivos que corresponden a las biomoléculas que seleccinaron [en ésta carpeta](https://drive.google.com/drive/folders/1ZvdIAHk12rULTPYz7MnXT3OeGZD0uBjF?usp=share_link). Este archivo tiene un formato especial que es conocido como `FASTA`. Los archivos con formato `FASTA` son comunes en la bioinformática pues son archivos de texto plano con secuencias de ácidos nucleícos o aminoácidos. A continuación un ejemplo: 

```
>NZ_CP010822.1 Thermus aquaticus Y51MC23 chromosome, complete genome
GTGGCCTTGACGCACGAGGCGGTCTGGCAGCACGTTCTGGAGCACATCCGCCGCAACATCACCGAGGTGGAGTACCACACCTGGTTTGAAAGGATCCGCCCCCTGGGTATCCGGGAAGGGGTTTTGGAGCTGGCGGTGCCCACCTCCTTCGCCCTGGACTGGATCAAGCGGCACTACGCCCCCCTGATCCAGGAGGCTTTAGGCCTCCTGGGGGCCCAGGTACCCCGCTTTGAGCTTTTGGTGGTGCCCGGAGCGCCCAGCCGGTCCAGGTGGACATCTTCCAGGCCGTCCCCCAGGCCGACCAGGGGAAGTCCAAGCT
```

La primera línea inicia con el símbolo `>` e indica un encabezado, que es información sobre la secuencia en cuestión. La segunda línea es la secuencia. Considera ésta información para el desarrollo de tu programa. Asegúrate que tu archivos tenga sólo **dos líneas**.

3. Contesta las siguientes preguntas sobre **una** de las biomoléculas que seleccionaro: 

  * ¿De qué organismo se trata? Haz una breve descripción del organismo. Te recomiendo que des click en el link que está en la [lista de proteínas](https://docs.google.com/spreadsheets/d/1UKyPqcmmgYuCQQb5_Zoyt-pTuSA4itq7/edit?usp=share_link&ouid=117981748854039384449&rtpof=true&sd=true) para darte una idea.
  * El organismo, ¿Es un eucarionte o un procarionte? Justifica apropiadamente tu respuesta.
  * La secuencia en cuestión, ¿Se trata de un gen o un genoma? Justifica apropiadamente tu respuesta.
  * ¿Ésta proteína es única en el organismo? Sino es el caso, ¿Qué otros organismos la presentan? Cita apropiadamente las fuentes que consultaste.
  * ¿Cuál es la función general de la proteína? Cita apropiadamente las fuentes que consultaste.
  
Las respuestas a éstas preguntas deben estar en el archivo `PDF`, recuerda que debe tener el siguiente formato: `p1_ApellidoNombre_cuestionario.pdf`

4. Crea un programa donde apliques los procesos del dogma central de la biolgía molecular, considera que la dirección de las secuencias van de 3'-5'. 

  * El programa debe aceptar como argumento un archivo en formato `FASTA` y debe arrojar como resultado:

  1. La cadena complementaria. 
  2. La secuencia transcrita, es decir, la cadena de RNA.
  3. La secuencia de aminoácidos. El programa debe asumir que el primer codón de la secuencia es un codón de inicio para que la secuencia pueda ser traducida, si el primer codón no es un codón inicio, el programa debe terminar. 

```{warning} **Consideraciones importantes**
**1. Sobre el programa:** 

  * Durante la traducción, es probable que no todos los codones de la cadena de DNA codifiquen para un aminoácido, para éstos codones que el programa arroje un `-` (guión).

  * [Aquí](https://drive.google.com/file/d/1G2J7eaoXXF6V9soCa7N0hGSauTb8tuxp/view?usp=share_link) hay un diccionario con el código genético por si te es útil.

  * El programa debe ser genérico, es decir, debe funcionar con cualquier archivo que se ingrese.

  * Deben asumir que el usuario es una persona que con mucho esfuerzo sabe correr un script de `python` en una terminal. Si hay algún error, no se va a molestar en revisarlo y tratar de solucionarlo. El usuario  debe entender los resultados que arroje el programa.

  * No puden utilizar ninguna paquetería de Python que ya tenga implementadas las funciones para hacer esto.

**2. Sobre la práctica en general.** 

  * Asegúrate de contestar con un lenguaje apropiado las preguntas del cuestionario. 

  * El plagio será penalizado.
```