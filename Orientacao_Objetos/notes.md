**Definição de Programação Orientada à Objetos:**
Um paradigma de programação que modela os dados e comportamentos como se fossem objetos do mundo real

**Objetos possuem:**
1. Propriedades (características)
2. Comportamentos (ações)

*objetos não são apenas variáveis, são autocontidos e reutilizáveis*
*os códigos mostram quem é o ator (objeto) e qual é o comportamento que está sendo invocado (método)*

**Classe:**
* estrutura usada para definir um novo tipo de dados
* descreve o que um objeto vai ser, mas não cria o objeto
* para criar um objeto, deve-se definir uma instância
* uma classe pode ter múltiplas instâncias
* sempre possuem o nome no singular
* permite criar coleções de objetos do mesmo tipo
* toda classe tem um método especial chamado construtor

**Construtor __ init __:**
* método especial
* inicializa o novo objeto da classe com seus valores padrão

**Método:**
* a diferença entre um método e uma função é que aquele é
associado a uma classe e atua sobre um objeto
* o primeiro parâmetro do método é chamado "self" e representa
a instância sobre a qual o método atuará

**Parâmetro especial 'self':**
* indica a instância da classe que está sendo considerada
* self.*name* cria um atributo, e não uma simples variável
* atributos definidos dentro de self podem ser acessados por
qualquer método dentro da classe
* não é necessário passar o parâmetro self ao chamar os métodos
da classe, o próprio interpretador o faz automaticamente

*Convenção para nomes de classes: PascalCasing*

**Função especial __ str __:**
* mostra o status do objeto

**Encapsulamento:**

* "tranca" o código, não permitindo alteração pelo usuário
* convenções utilizadas:
    * _(underscore) = protegidos - algumas exceções de acessos
    * __(undescore duplo) = pricados - não acessados de forma nenhuma


**Propriedades:**

* se parecem com os atributos, mas na verdade usam métodos por
traz do pano
    * @property        (getter -> chama a propriedade)
    * @classe.setter   (setter -> permite realizar alteração)


**Herança:**
* uma classe pode herdar os métodos e atributos de outra classe
* permite adicionar funcionalidades sem modificar uma classe já
existente, criando uma classe derivada (ou filha)
* se a classe B herda a classe A, todos que herdam a classe B
também herdam a classe A (transitividade)

        class Classe_B(Classe_A)
            def __init__()
            super().__init__()       
            #chama o construtor da classe base

        def funcao_classe_A(self)    
            self._variavel = 'novo_valor'
            return super().funcao_classe_A
            # sobrescreve a função original da Classe A

*Verificando a instância do objeto:*

    isinstance(objeto, Classe)
    issubclass(Classe_B, Classe_A)

* todas as classes herdam implicitamente da classe object do Python

         dir()   #mostra todas as classes


**Classe abstrata:**
* é considerada como um modelo para criar outras classes
* funciona como um 'template'
* precisa ter um ou mais métodos/propriedades abstratos
que deve ser implementados pelas classes filhas
* usar a biblioteca ABC (Abstract Base Classes)
* métodos abstraatos são marcados com o decorator *@abstractmethod*
* são usadas para definir a API (application programm interface)
 das classes filhas
* garante a previsibilidade


**Tratamento de exceções:**

    try [...]
    except [...]

**Executar debug no VSCode:**

-> adicionar ponto de parados

-> executar Run e Debug

-> selecionar python file

**Modelagem de um sistema orientado a objetos:**
* a POO cria modelos do mundo real
* os modelos possuem classe que representam atores do mundo 
real
* durante a modelagem, você examina uma descrição de um domínio
e tenta analisar os atores e as regras de negócio
* atores atuam no domínio e executam uma ação
* atores costumam atuar sobre dados, que são a entrada necessária
para executar uma ação
* o que os atores fazem para executar essa ação é chamado
de comportamento
* atores podem interagir uns com os outros para chegar a um
resultado
* o resultado da atuação e intereção entre os atores gera uma
saída
* em resumo, MODELAGEM é o processo de identificar os ATORES,
os DADOS necessários e o tipo de INTERAÇÃO que está ocorrendo.
Para criar um sistea, é necessário conhecer suas REGRAS DE 
NEGÓCIO