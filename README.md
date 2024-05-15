# HASHTAG_Python_PowerUP
Curso Hashtag - Jornada Python - 1_Power UP 2024/05

## Instruções do Curso sobre "Projeto de Automação" em Python

O objetivo é criar um projeto de automação para cadastro e inclusão de intens em um determinado repositório para consulta futuras, mas tudo feito de modo automático a partir de comandos realizados em Python.

### (P) Passo a passoa da realização do projeto:

#### Realizar a elaboração da lógica de programação para que todas as atividades necessárias sejam atingidas. 'Dessa forma, vamos escrever a realização de cada ação para a construção do código de forma didática, unindo a lógica de programação com a linguagem de programação'.

##### Então, digamos que uma determinada empresa tenha uma base de dados e deseja cadastrar vários produtos e entrega ao funcionário essa missão. Logo, os passos para criação da automação seriam:

##### P1 - Abrir o sistema da empresa
##### P2 - Fazer o login
##### P3 - Abrir/importar a base de dados de produtos para cadastrar
##### P4 - Cadastrar um produto
##### P5 - Repetir os passos anteriores até finalizar os cadastros

#### A partir daqui vai ser feito didaticamente a escrita do código com explicações simplistas (minimizando as tecnicas, mas melhorando a assimilação do aprendizado)

##### Vamos começar o P1

###### A ideia é realizar a abertura do site da 'empresa' para fazer o login. Então os passos serão, clicar na tecla windows do teclado -> digitar chrome -> pressionar enter no teclado -> (ao abrir a janela do browser) digitar o site/link da empresa (site fornecido para o teste pela hashtag = https://dlp.hashtagtreinamento.com/python/intensivao/login)...

###### P1.1 Porém, para realização desses passos anteriores, e de forma automatizada, tem que ser através da instalação de uma biblioteca do python, chamada 'pyautogui' através da abertura do terminal 'cmd' e o uso do código:

pip install pyautogui

###### P1.2 Findada a instalação, agora deve-se fazer a importação dessa biblioteca através do comando:

import pyautogui

###### P1.3 Pronto, em toda a escrita do código, sempre que necessária a utilização de alguma função dessa biblioteca, após a importação é só digitar:

pyautogui. (a partir do '.' é disponibilizada uma lista de funções para melhor atender a necessidade do programador)

###### Assim, pelo Python ser uma linguagem de alto nível, sendo projetada para ser mais próxima da linguagem humana, facilita a sua compreensão e uso, então, no código que será inscrito, precisa-se informar através da biblioteca pyautogui as funções que executem os passos ditos anteriormente, (obs.: cada código deve ser digitado um abaixo do outro para leitura mecânica, sendo encadeado o parâmetro necessário que funcione a partir da orientação anterior), assim:

###### P1.4 clicar na tecla windows do teclado 

pyautogui.press("win") -> vai ser 'pressionado'(press - na realidade aciona a tecla win='windows' no sistema).

###### P1.5 digitar chrome

pyautogui.write("chrome") -> vai ser 'escrito'(write - digitada o que se está entre as aspas e no exemplo, vai ser escrito 'chrome' no buscador do windows).

###### P1.6 pressionar enter no teclado 

pyautogui.press("enter") -> vai ser 'pressionado'(press - na realidade aciona a tecla enter='entrar/confirmar' no sistema). Obs.: a configuração do browser do chrome já deve abrir a janela com a barra de navegação ativada para digitação, ter atenção para esse detalhe.

###### P1.7 (ao abrir a janela do browser) digitar o site/link da empresa (site fornecido para o teste pela hashtag = https://dlp.hashtagtreinamento.com/python/intensivao/login)

pyautogui.write("https://dlp.hashtagtreinamento.com/python/intensivao/login") -> vai ser 'escrito'(write - digitada o que se está entre as aspas). 

###### P1.8 pressionar enter no teclado 

pyautogui.press("enter") -> vai ser 'pressionado'(press - na realidade aciona a tecla enter). Obs.: ao tentar escrever todo esse link, a velocidade da ação de programação e o processamento de dados do computador podem entrar em conflito e a execução do código não ser apresentada, mesmo que seja 'realizada'. Então, para que se evite esse 'atropelamento' de execução das ações, é inserido uma configuração do 'pyautogui' chamada 'PAUSE' logo após sua importação para que seja realizada de maneira "cadenciada" cada ação de acordo com o tempo que se é estipulado na configuração.

###### P1.9 Uso da configuração temporizadora do pyautogui

pyautogui.PAUSE = tempo declarado respeitando o padrão EUA '.' para separar casas decimais. Dessa forma, após a importação do 'pyautogui', vem essa configuiração temporizadora.

###### P1.10 Tempo de oscilação da internet

Visto que após inserir na barra de endereço do browser o site/link tem algum delei a depender da internet, então, importa-se a biblioteca 'time'

import time

###### P1.10.1 Especificação do tempo determinado para realização do parâmetro após a inserção do 'time' junto a função 'sleep' determinando um tempo só nesse ponto

time.sleep() -> insere o tempo desejado que o código anterior seja executado a partir daquele ponto vai ficar em "espera" e por seguinte vai continuar a execuação de acordo com o tempo pré-definido por 'PAUSE'

##### Vamos começar o P2

###### A realização de login ocorre a partir do usuário 'utilizar'(na realidade, vamos orientar o sistema para o lugar exato na atuação do clique) o mouse e clicar no campo de inserção do email, normalmente. Assim, terá que fazer o uso do 'pyautogui.click'. Todavia, esse recurso precisa de uma localização/posição de onde será feito esse clique, chamamos de coordenadas 'x e y' da posição do mouse. Portanto, ao disponibilizar os parâmetros para a função 'click(x,y)' terá o lugar exato do clique. Mas para isso, vai ser necessário uma 'manobra' no código em que será criado um novo arquivo python de nome qualquer ('position.py') para que através da importação das bibliotecas 'pyautogui' e 'time', possa ser feito uso da função 'sleep(tempo necessário, vai depender do computador) e a coleta da posição por meio do 'print' da função 'position()' escrita no código.

import pyautogui
import time

time.sleep(7.0)

print("pyautogui.position()")

###### P2.1 Posição do clique para realização do login

Feita a coleta dos valores das coordenadas(x,y), insere-as na função 'pyautogui.click(x,y)'

pyautogui.click(x,y,'personalização') -> após as coordenadas essa função pode ainda ser personalizada:

* quantidade de cliques: pyautogui.click(x,y,clicks=5) serão 5 cliques;
* pode indicar que botão do mouse: pyautogui.click(x,y,button="right") clique será com o botão direito;

###### P2.2 vamos repetir passos anteriores 'write' e 'press'

pyautogui.write("email") -> digita o email do login
pyautogui.press("tab") -> vai saltar para o próximo campo
pyautogui.write("senha") -> digita a senha
pyautogui.press("tab") -> vai para o botão do site
pyautogui.press("enter") -> confima para ir ao cadastro

time.sleep(4.0) -> determinar um tempo para após o login

##### Vamos começar o P3

###### Após logar na página de cadastrar, agora será necessário fazer a importação da base de dados de algum arquivo dessa especificação, seja csv, sql, xls ou qualquer outro que armazene dados. Então, deve-se fazer a instalação de uma biblioteca que trate esses dados, logo, usa-se o 'pandas'. Portanto, no terminal cmd usa o código 'pip install pandas', porém, para ajudar esse código em complemento, instala-se o 'numpy' e o 'openpyxl' que são funcionalidades adicionais para conjunto com o 'pandas':

pip install pandas numpy openpyxl

###### P3.1 importação da biblioteca 'pandas'

import pandas as pd -> 'as' é o como, usado para possibilitar um "apelidio" para biblioteca (o 'pd' é uma norma mundial usado como apelido para o pandas)

###### P3.2 leitura da base de dados

###### Através do 'pd'(pandas) e sua função de leitura 'read' é que se faz agregação da base de dados para possível uso, então escreve o código:

pd.read_csv("nome do arquivo.extensão que é especificada na função 'read' da biblioteca")

###### No entanto, só a realização da inserção desse código não teria funcionalidade. Então, para que seja possível a sua utilização, terá que criar variáveis para agregar os dados e sejam feitas as leituras e uso deles. Logo, ao criar uma variável como o nome genérico (mas de preferência que seja consenso para o seu entendimento e de programadores que poderão utilizar) deve-se 'receber' o equivalente a sua igualdade, portanto:

tabela = pd.read_csv(nome_dos_dados) -> a leitura desse código será, a variável 'tabela' recebe os dados de tudo o que está após a igualdade

###### Repetiu-se o passo 'P2.1 Posição do clique' para que começar o cadastros dos itens.

##### Vamos começar o P4

###### Este será o momento do cadastro dos produtos. Porém, quando se deseja fazer uma ação repetitiva que envolva os mesmos passos, para melhor resultado do planejado, deve-se fazer a ação para um item. Sendo bem sucedido o objetivo, logo, poderá criar o laço de repetição para os próximos. Então, a partir do exemplo de cadastro de um item qualquer que está entre os contidos no banco de dados, vai-se orientar a realização dos passos-a-passos através dos códigos já utilizados anteiormente ('write' e 'press'), mas com os dados atualizados:

###### Porém, vamos criar uma variável para o código

codigo = "MOLO000251"
pyautogui.write(codigo) -> digitar o código
pyautogui.press("tab") -> vai saltar para o próximo campo

marca = "Logitech"
pyautogui.write(marca) -> digitar o código
pyautogui.press("tab") -> vai saltar para o próximo campo

tipo = "Mouse"
pyautogui.write(tipo) -> digitar o código
pyautogui.press("tab") -> vai saltar para o próximo campo

categoria = "1"
pyautogui.write(categoria) -> digitar o código
pyautogui.press("tab") -> vai saltar para o próximo campo

preco_unitario = "25.95"
pyautogui.write(preco_unitario) -> digitar o código
pyautogui.press("tab") -> vai saltar para o próximo campo

custo = "6.50"
pyautogui.write(custo) -> digitar o código
pyautogui.press("tab") -> vai saltar para o próximo campo

obs= ""
pyautogui.write(obs) -> digitar o código
pyautogui.press("tab") -> vai saltar para o próximo campo

###### No entanto, todo esse código foi realizado, praticamente, manualmente. Assim, precisando de um tratamento para automação, visto que o banco de dados pode ser feita a leitura em todas as suas linhas para que possam também, serem coletados esses dados. 

##### Vamos começar o P5

###### Então, é necesário que o código seja decorrido para cada linha da tabela de dados. Portanto, através de um laço/matriz('for') é possível a repetição e orientação de linha em linha do código.

for linha in tabela.index: -> pode ser lido: 'for'(para cada) linha(variável representa todos os itens da linha do banco de dados) in(dentro da) tabela.index(tabela é a variável função do banco de dados; index é a função que coleta os intens contidos em um banco de dados por linha)

###### P5.1 Dessa forma, vai ser feita a utilização do código acima com a identação do cadastro genérico dos itens da tabela, tão quanto o clique('click(x,y)') para que a repetição do laço sempre inicie do mesmo lugar (campo código). Então:

for linha in tabela.index:
    click(x,y)
    codigo = "MOLO000251"
    pyautogui.write(codigo) -> digitar o código
    pyautogui.press("tab") -> vai saltar para o próximo campo

    marca = "Logitech"
    pyautogui.write(marca) -> digitar o código
    pyautogui.press("tab") -> vai saltar para o próximo campo

    tipo = "Mouse"
    pyautogui.write(tipo) -> digitar o código
    pyautogui.press("tab") -> vai saltar para o próximo campo

    categoria = "1"
    pyautogui.write(categoria) -> digitar o código
    pyautogui.press("tab") -> vai saltar para o próximo campo

    preco_unitario = "25.95"
    pyautogui.write(preco_unitario) -> digitar o código
    pyautogui.press("tab") -> vai saltar para o próximo campo

    custo = "6.50"
    pyautogui.write(custo) -> digitar o código
    pyautogui.press("tab") -> vai saltar para o próximo campo

    obs= ""
    pyautogui.write(obs) -> digitar o código
    pyautogui.press("tab") -> vai saltar para o próximo campo

###### Porém, uma observação a ser feita é que ao fazer o cadastro do 1º produto, após a confirmação('enter'), a página deve ser rolada para o ínicio, visto que ao ser inseridos os dados, a tela vai acompanhando os passos e descendo até o pornto de envio. Dessa forma, no 'for', deve ter inserido o código para que a tela seja rolada para o topo. Então, através do código:

pyautogui.scroll(5000) -> número especificado para subir a tela, varia de computador para computador junto a resolução da tela. Portanto, usar um valor alto para não correr risco de não trazer a tela; 

###### Outra alternativa:

pyautogui.press("home")

###### P5.2 Apesar de o código está atuando de maneira planejada, ainda não realiza a coleta dos dados linha por linha, seguindo as colunas dos dados. Então, através de um método da biblioteca 'pandas'(pd) é que será possível fazer essa ação. Logo, onde se tem a célula da tabela que se planeja coletar os dados, usa-se 'tabela.loc[linha, coluna]', especificando a 'linha'(todavia, neste exemplo estamos já coletando as linhas(index), assim, o código já decorre as linhas uma a uma) e a 'coluna'(no exemplo, vai ter que ser escrito o nome do cabeçalho das colunas, sendo fiel a cada caractere existente na tabela, então, qualquer alteração, será tido como erro ao executar o código - no banco de dados produtos.csv o cabeçalho das colunas tem estes nomes: codigo,marca,tipo,categoria,preco_unitario,custo,obs; sendo importante a construção do código com esses mesmos itens). Portanto:

for linha in tabela.index:
    click(x,y)
    codigo = tabela.loc[linha,"codigo"]
    pyautogui.write(codigo)
    ...

###### P5.3 Porém, uma atenção que deve ser dada para essa construção é que os itens que compõem as colunas, devem ser "tratados" para que a biblioteca 'pandas' configure os dados numéricos para string('str'-texto). Portanto, para que não se corra o risco de possíveis erros, todos as colunas já devem ser transformadas em texto, então, usa o tabela.loc[] para todos os códigos que serão necessários coletar os dados da tabela, sendo envolvidas pelo tratamento 'str()':

for linha in tabela.index:
    click(x,y)
    codigo = str(tabela.loc[linha, "codigo"])
    pyautogui.write(codigo)
    pyautogui.press("tab")
    pyautogui.write(str(tabela.loc[linha, "marca"])) 
    pyautogui.press("tab")
    pyautogui.write(str(tabela.loc[linha, "tipo"]))
    pyautogui.press("tab")
    pyautogui.write(str(tabela.loc[linha, "categoria"]))
    pyautogui.press("tab")
    pyautogui.write(str(tabela.loc[linha, "preco_unitario"]))
    pyautogui.press("tab")
    pyautogui.write(str(tabela.loc[linha, "custo"]))
    pyautogui.press("tab")
    pyautogui.write(str(tabela.loc[linha, "obs"]))
    pyautogui.press("tab")
    pyautogui.scroll(5000)

###### P5.4 visto que nos campos sem dados, a biblioteca 'pandas'(pd) incluí o termo 'nan' por padrão. Então, deve-se ser feito um tratamento para evitar esse autocomplete. Assim, através do tratamento por meio de uma condicional é possível corrigir essa ação. Portanto, o campo que ocorre o 'nan' é o 'obs'. Dessa forma, cria-se uma variável para o 'obs', pois, o único intuíto é o não preenchimento.

for linha in tabela.index:
    click(x,y)
    codigo = str(tabela.loc[linha, "codigo"])
    pyautogui.write(codigo)
    ...
    obs = (str(tabela.loc[linha, "obs"])) -> variável 'obs'
    if obs != "nan": -> if(se) obs(variável para o campo obs) !=(é diferente de) "nan"(string nan):
        pyautogui.write(obs) -> então, essa linha será executada, caso a condição acima seja verdadeira 
    pyautogui.press("tab")
    pyautogui.press("enter")
    pyautogui.scroll(5000)

# PROJETO COMPLETO