<h1 align="center">Gerenciador de Operações - Casa de Câmbio Muito Dinheiroo</h1>

<h2>Descrição</h2>
<p>Este repositório contém o gerenciador de operações da casa de câmbio Muito Dinheiro, que tem como objetivo facilitar a realização de atividades rotineiras e documentar operações.</p>
<p>Este gerenciador foi escrito em linguagem Python utilizando como IDE o Notebook Google Colaboratory, é composto por uma calculadora de conversões que realiza as operações matemáticas para converter as moedas de acordo com a solicitação do usuário, bem como, fornecer um panorama préveio das operações realizadas.Conta também com um bloco de instruções onde é possível realizar filtros por nome do cliente, intervalo de data da operação e por nome do cliente e intervalo de data da operação, exibindo ao usuário um banco de dados filtrado e com valores totais das operaçõs realizadas e das taxas cobradas. </p>

<h2>Como Usar</h2>
<p>Para usar este gerenciador basta abrir o código exatamente como está descrito no arquivo gerenciador.py em um arquivo do Google Colaboratory, ou um Jupyter Notebook, podem ser usadar também IDEs instaladas na própria máquina como o PyCharm, o IDLE e qualquer outro de preferência do usuário. Basta executar o código e preencher os códigos conforme orientado pelo próprio programa, mas se mesmo assim ficou confuso, não se preocupe! Veja a descrição mais detalhada a seguir...</p>

<p>a) O primeiro passo é preencher o campo de texto com a opção desejada, isto é, escolher entre:</p>
<p>1 - Novo Cadastro</p>
<p>2 - Relatório</p>
<p>Neste primeiro momento basta escrever o número 1 ou o número 2 na caixa de texto e pressionar a tecla enter, escrevendo o núemro 1 você inicia o cadastro do cliente e prossegue para a calculadora de conversões; escrevendo o número 2 você pula para a geração do relatório de operações, que só será últil pós cadastrar clientes!</p>
<br>
<p>b) Em seguida, você deve preencher o nome do cliente, de forma simples, sem acentuações, para facilitar sua busca dentro do relatório posteriormente, por exemplo, se o nome de seu cliente é João Paulo Silva, você pode simplesmente preencher o compo com: joao paulo silva e pressionar a tecla enter</p>
<br>
<p>c) O próximo passo é preencher a data da operação, que deve ser preenchida no forma dia/mês/ano, por exemplo, 20/05/2020. Digite todos os números e todas as barras sem espaços e pressionar a tecla enter!</p>
<br>
<p>d) No próximo passo, o programa irá exibir uma lista de moedas e suas cotações correspondentes em reais, e perguntar se você deseja cadastrar uma nova moeda (1) ou não (2), basta digitar o número 1 ou o número 2 e pressionar a tecla enter (caso digite o número 2, pule para a letra (h))</p>
<p>e) Digitando o número 1, você deverá responder em seguida quantas novas moedas você deseja cadastras. Suponhamos que você deseja adicionar as moedas JPY e CLP à lista, com as seguintes cotações: 0.049 e 0.0073, respectivamente. Para isso, será necessário adicionar 2 novas moedas à lista, então, responda a pergunta com o número 2!</p>
<br>
<p>f) Insira o código/sigla da moeda que você deseja cadastrar primeiro, no nosso exemplo, você digitaria o JPY, e na próxima pergunta você digitaria o valor da moeda em reais, 0.049.</p>
<p>g) O mesmo se repetiria para o CLP, com o valor 0.0073</p>
<br>
<p>h) Neste campo você deve digitar o código que você vê na linha acima aos nomes das moedas, que estão exibidas na tela, por exemplo, a moeda EUR tem o código 0, e a moeda USD tem o código 1. Apenas digite o número correspondente à moeda de origem e pressione enter</p>
<br>
<p>i) Digite o valor que você pretende converter em outra moeda, por exemplo, se você tem 200 euros e pretende convertê-los em dóleres americanos, digite 200 e pressione a tecla enter.</p>
<br>
<p>j) Agora você deverá digitar o código da moeda de destino, do mesmo jeito que você fez na instrução (h), mas agora é para a moeda em que você quer converter o seu dinheiro! Para converter em dólares americanos (USD), por exemplo, você deveria digitar o número 1 e pressionar a tecla enter</p>
<br>
<p>k) No próximo passo todas estas operações se repetem até que você cadastre tantos clientes quanto queira, para passar para a execução do relatório, basta digitar a opção 2!</p>
<br>
<p>l) Ao escolher a opção 2 na lista abaixo, você será direcionado para o relatório de operações</p>
<p>1 - Novo Cadastro</p>
<p>2 - Relatório</p>
<p>m) No próximo passo, você terá a opção de digitar a letra R para gerar um relatório ou digitar a letra S para encerrar o programa, digite uma das letras (maiúscula ou minúscula e sem espaços) e pressione a tecla enter.</p>
<br>
<p>n) Em seguida, você deve escolher uma das opções a seguir para executar o filtro nas operações que foram realizadas durante a execução do programa, digitando o número correspondente na caixa de texto, sem espaços, e pressionando a tecla enter</p>
<p>1 - Filtrar por nome</p>
<p>2 - Filtrar por intervalo</p>
<p>3 - Filtar por nome e intervalo</p>
<br>
<p>Se você digitar o número 1, deverá preencher a próxima caixa de texto com o nome do cliente que você procura, é recomendado digitar o nome sem acentuações,bem como feito no cadastro inicial (instrução (b)), para que você consiga filtrar com êxito.</p>
<br>
<p>Se você digitar o número 2, deverá preencher a data inicial e a data final do intervalo em que deseja filtrar suas operações, no mesmo formato das datas cadastradas, conforme a instrução (c) </p>
<br>
<p>Por fim, se você digitar o número três, deverá preencher tanto o nome do cliente, quanto o intervalo de datas, filtrando assim as operações que ocorreram em um determinado paríodo para um determinado cliente.</p>
<br>
<p>Após isso, o programa exibirá os resultados de acordo com o filtro aplicado, bem como os totais das operações realizadas e das taxas cobradas em forma de tabela.</p>





