#importar el paquete ggplot 2
library(ggplot2)

# crear un gráfico de dispersión
ggplot(data, aes(x = x, y = y)) + geom_point()