# My-very-big-Python

## 1.1. Antecedentes

LACAY requiere un software que le permita manejar:
- Personal
- Carta y Recetas
- Compras y Ventas
- Publicidad

## 1.2. Manejo de Personal

El software a construir tendrá un mantenimiento de cargos y de personal (crear, consultar, modificar, eliminar y reportar). Los cargos tendrán la siguiente información:
- Identificador
- Nombre del Cargo
- Jefatura

Cuando un cargo puede tener personal bajo su responsabilidad, se entiende que es un cargo de Jefatura. Un ejemplo de un cargo de Jefatura podría ser el jefe de Chefs que tiene muchos Chefs a su cargo. Algunos cargos son de jefatura, otros no.

Note que varias personas pueden tener el mismo cargo (por ejemplo, puede haber varios chefs en un restaurante…), pero una persona solo puede tener un cargo en la cadena de restaurantes.

También se requiere un mantenimiento de Personal. Los datos de personal son:
2
- Cédula (validar que se trate de una cédula correcta)
- Apellidos
- Nombres
- Fecha de Nacimiento
- Dirección
- Cargo
- Jefe

El personal siempre tendrá un cargo, por lo tanto, se requiere que exista al menos 1 cargo creado antes de crear un personal. Siempre tendremos un Gerente General, por lo que el software por defecto deberá ya tener creado el cargo Gerente General y al personal que es el Gerente. En el Campo Jefe del Gerente, se colocará a sí mismo. Obviamente, al crear un personal, distinto al Gerente y acceder a definir su cargo o su jefe, el software debería desplegar, de alguna forma los cargos y los jefes que podrían seleccionarse, es decir los que están ya creados en el software.

A veces se requiere eliminar a un personal, pero hay que tomar ciertas precauciones. Por ejemplo, si el personal A es jefe de B y de C, y si eliminamos a A, B y C no tendrían un jefe. Eso no es factible. El software debería evitar ese tipo de situaciones. Algo similar ocurriría al eliminar un cargo.

El software debería generar unos reportes específicos:
- Jefe y su personal a cargo
- Cargos y personal con ese cargo

## 1.3. Manejo de Carta y Recetas

Una carta es un conjunto de platos y un plato se logra con un conjunto de ingredientes y una preparación.

El software deberá permitir el mantenimiento de ingredientes, un ingrediente tiene los siguientes datos:
- Identificador
- Nombre
- Unidad
- Existencia (cantidad de unidades disponibles en stock)
- Perecible

También debe ser posible manejar un mantenimiento de platos(receta):
- Identificador
- Nombre
- Tipo
- Ingredientes
- Preparación

Los ingredientes de un plato deberán seleccionarse de los existentes, además por cada ingrediente se debe indicar la cantidad que se empleará en el plato. La preparación será un texto de máximo 250 caracteres. Note que estas recetas son para la elaboración de 1 unidad del plato. En cuanto al tipo, un plato puede ser entrada, plato fuerte o postre.

LACAY prepara su carta organizada por tipo de plato. El software deberá mostrar una carta digital con la lista de platos por tipo.

## 1.4. Compras y Ventas

Cada vez que se compra un producto se deberá registrar un ingreso al inventario.

El ingreso contará con fecha de adquisición, el costo del producto, la cantidad de productos adquiridos y se apuntará al producto.

Los ingresos actualizarán el campo Existencias del producto correspondiente. 

Cuando un producto tenga una existencia pequeña, el software debería alertar sobre la necesidad de abastecerlo.

El departamento de ventas deberá definir el precio de venta de los platos, lo hará en base a lo siguiente: 
sumatoria de costo de ingredientes + 10% en caso de existir al menos un producto perecible, por concepto de almacenaje + 40% por costo de preparación + 25% de utilidad. 

Los precios deberán mostrarse en la carta digital y podrían variar en el tiempo. Note que los precios dependen de los costos de los productos a emplear y de los porcentajes vigentes (los porcentajes podría también variar!)

Al vender un plato se están generando egresos de los inventarios de productos, esto actualizará el campo Existencia de los productos y consumirá los productos de algún ingreso. Los productos perecibles deberán manejarse con un inventario FIFO y los no perecibles con uno LIFO.
Un egreso a un inventario, también tendrá una fecha.

Las transacciones de Compras y Ventas no podrán modificarse pero si eliminarse; en el caso de las Compras, solo si los productos del ingreso a eliminar no han sido usados en alguna venta.

Una Venta, guarda los platos, cliente, cupones y precio total. No se modifican ni eliminan.

## 1.5. Publicidad

Una campaña consiste de un nombre, un empleado encargado de ella, el costo de la campaña, el tipo y las fecha de inicio y finalización.

Las campañas pueden ser de tipo: red social, radio/TV, valla publicitaria, cupones. 

El equipo de publicidad de LACAY prepará varias campañas, que deberán ser registradas en el software. 

Las campañas pueden ser creadas, consultadas, reportadas, eliminadas y modificadas.

Las eliminaciones y modificaciones aplican solo a campañas que no estén vigentes. 

El reporte debe incluir un listado de todas las campañas, inclusive de las eliminadas… por lo tanto se deberá manejar una eliminación lógica y no física.

Las campañas tipo cupones sirven para motivar a las personas a ir al Restaurante, por ejemplo un cupón para un 15% de descuento en sus compras.

El sistema debería guardar la identificación del cliente que tiene el cupon y el porcentaje de descuento. Esto se usará para validar cupones durante las ventas.
