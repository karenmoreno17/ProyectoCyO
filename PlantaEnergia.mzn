% Problema de las plantas de energía.
% Autores:
%  * Alvaro Portocarrero.  1922171.
%  * Juan David Cabrera.   1924619.
%  * Karen Daniela Moreno. 1922373.

include "Datos.dzn";

% Matriz con la cantidad de MW generados por día en cada central.
array [1..N, 1..3] of var int: generadoDia; 

% Arreglo de la cantidad de MW recibidos por cada cliente.
array [1..N, 1..M] of var int: vendidoDia;

% Condición: No negatividad.
constraint forall(i in 1..N, j in 1..3)(
  generadoDia[i, j] >= 0
);

% Condición: La cantidad vendida al día a un cliente se encuentra entre
%   la demanda del día y un porcentaje mínimo establecido.
constraint forall(i in 1..N, j in 1..M)(
  vendidoDia[i, j] <= DEMANDA[i, j] /\ vendidoDia[i, j] >= G*DEMANDA[i, j]
);

% Condición: La cantidad generada no excede el máximo por central.
constraint forall(i in 1..N, j in 1..3)(
  generadoDia[i, j] <= MAXXCENTRAL[j]
);

% Condición: El total vendido al día es igual a lo generado ese día.
constraint forall(i in 1..N)(
  sum(j in 1..M)(vendidoDia[i, j]) == sum(j in 1..3)(generadoDia[i, j])
);

% Condición: Restricción de régimen alto.
constraint forall(i in MAXREGALT..N)(
  sum(j in 0..MAXREGALT-1)(generadoDia[i-j, 2] >= REGALT*MAXXCENTRAL[2]) < MAXREGALT
);

solve maximize sum(i in 1..N, j in 1..M)(
  vendidoDia[i, j]*PRECIOXCLIENTE[j]
) - sum(i in 1..N, j in 1..3)(
  generadoDia[i, j]*COSTOXCENTRAL[j]
);

output["Generado por las centrales: ",show(generadoDia),".\nVendido: ",show(vendidoDia),"\nDemanda: ",show(DEMANDA)];