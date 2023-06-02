# Estudos sobre Classes e Orientação a Objetos

Este é um repositório dedicado a um projeto/exercício de Classes, Orientação a Objetos e exercícios complementares.

# Gerador de Senha

A parte mais difícil de gerenciar várias contas é gerar uma senha forte diferente para cada uma.
Uma senha forte é uma mistura de letras, números e caracteres alfanuméricos. Portanto, o melhor
uso do Python seria criar um projeto em que você pudesse gerar senhas aleatórias para qualquer
uma de suas contas.

Para criar uma senha forte, os usuários podem usar este gerador de senha para gerar uma senha
aleatória e personalizada.

Etapas necessárias para a construção deste projeto:

        1. Todos os caracteres devem ser armazenados como uma lista.
        Ps.: Isso pode ser feito com o módulo string do Python ou digitando cada caractere individualmente.

        2. Peça ao usuário o comprimento da senha.
        
        3. Use random.shuffle para embaralhar os caracteres.

        4. Crie uma lista vazia para armazenar a senha.
        
        5. Repita os processos abaixo para gerar a senha até atingir o comprimento da senha.

        6. Escolha um caracter aleatório de todos os caracteres usando o método random.choice.

        7. Adicione o caractere aleatório à senha.

        8. Randomize a lista resultante de senhas.

        9. Use o método join para criar uma string da lista de senhas.

        10. Imprima a senha.

* [Projeto Gerador de Senha 1](src/main.py)

2. Faça um Gerador de Senha somente com letras minúsculas e números.

* [Projeto Gerador de Senha 2](src/exercicio2.py)

3. Faça um Gerador de Senha somente com letras maiúsculas e números.

* [Projeto Gerador de Senha 3](src/exercicio3.py)

4. Faça um Gerador de Senha somente com números.

* [Projeto Gerador de Senha 4](src/exercicio4.py)

5. Faça um Gerador de Senha com 11 números e um validador para saber se a senha não é um CPF.

* [Projeto Gerador de Senha 5](src/exercicio5.py)

<!-- EXERCÍCIOS COMPLEMENTARES -->

# Exercícios Complementares

São exercícios de Classes retirados do site https://wiki.python.org.br/ExerciciosClasses.


4. Classe Pessoa: Crie uma classe que modele uma pessoa:

        I. Atributos: nome, idade, peso e altura

        II. Métodos: Envelhercer, engordar, emagrecer, crescer.

        Obs: Por padrão, a cada ano que nossa pessoa envelhece, sendo a idade dela menor que 21 anos, ela deve crescer 0,5 cm.
* [Exercício 1](exercicios/ex1.py)

8. Classe Macaco: Desenvolva uma classe Macaco, que possua os atributos:

        nome e bucho (estomago) e pelo menos os métodos comer(), verBucho() e digerir().

Faça um programa ou teste interativamente, criando pelo menos dois macacos,
alimentando-os com pelo menos 3 alimentos diferentes e verificando o conteúdo do estomago
a cada refeição. Experimente fazer com que um macaco coma o outro.
É possível criar um macaco canibal?


* [Exercício 2](exercicios/ex2.py)

# Licença

<img alt="License" src="https://img.shields.io/badge/license-MIT-%2304D361?color=rgb(89,101,224)">

Distribuído sob a licença MIT. Veja [LICENSE](LICENSE) para mais informações.

# Contato

Me acompanhe nas redes sociais.

<p align="center">


  <a href="https://www.instagram.com/ddavimig/" target="_blank" >
    <img alt="Instagram" src="https://img.shields.io/badge/-Instagram-ff2b8e?logo=Instagram&logoColor=white"></a>

  <a href="https://www.linkedin.com/in/davimss/" target="_blank" >
    <img alt="Linkedin" src="https://img.shields.io/badge/-Linkedin-blue?logo=Linkedin&logoColor=white"></a>

  <a href="mailto:davi00msantos@gmail.com" target="_blank" >
    <img alt="Email" src="https://img.shields.io/badge/-Email-c14438?logo=Gmail&logoColor=white"></a>

</p>