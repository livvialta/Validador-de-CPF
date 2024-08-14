# Descrição:
Esse código valida o CPF para verificar se ele é válido, com base no cálculo especificado pelo Ministério da Fazenda.

O CPF é formado por 11 números que seguem a máscara "xxx.xxx.xxx-xx", a verificação do CPF acontece utilizando os 9 primeiros números e, com um cálculo, é verificado se o resultado corresponde aos dois últimos dígitos (depois do sinal "-").

## Cálculo:

1. Multiplica-se os 9 primeiros dígitos numéricos pela sequência decrescente de números de 10 à 2 e soma os resultados;
2. Multiplicar esse resultado por 10 e dividir por 11;

O resultado que nos interessa na verdade é o RESTO da divisão. Se ele for igual ao primeiro dígito verificador (primeiro dígito depois do '-'), a primeira parte da validação está correta.

3. Agora é preciso multiplicar os 10 primeiros dígitos numéricos pela sequência decrescente de 11 a 2 e somar os resultados; 
4. Multiplicar por 10 e dividir por 11;

E  agora verificar o resto e se for correspondente ao segundo dígito verificador, é válido.

***Observação Importante: *** Se o resto da divisão for igual a 10, ele é considerado como 0.

## Importante considerar:
Existe alguns casos de CPFs que passam nessa validação que expliquei, mas que ainda são inválidos. É os caso dos CPFs com dígitos repetidos (111.111.111-11, 222.222.222-22, etc.)
Esses CPF atendem à validação, mas ainda são considerados inválidos.

No nosso código, vamos verificar se todos os dígitos do CPF são iguais e, se for o caso, considerar que ele é inválido.
