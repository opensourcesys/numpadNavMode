# Numpad Nav Mode #

# Modo de navegação do teclado numérico

* Autor: Luke Davis (Open Source Systems, Ltd.)
* Download [versão estável][1]

O Numpad Nav Mode é um complemento do [NVDA][2] que permite alternar
facilmente o teclado numérico do teclado entre os controles de navegação do
NVDA e os controles de navegação do Windows que não são de leitura de
tela. Isso pode ser especialmente útil para usuários que estão migrando do
Jaws para o NVDA. Esse complemento também oferece controle granular sobre a
alternância da tecla numlock, quando o NVDA é iniciado e, opcionalmente, nos
perfis.

### Explicação e recursos dos modos de navegação

As funções normais do teclado numérico do PC, com o numlock desativado, são:
page up, page down, home, end, teclas de seta de quatro direções e uma tecla
de exclusão.  Mas o NVDA assume completamente o teclado numérico para
fornecer teclas de revisão, controles de mouse e controles de navegação de
objetos. Isso ocorre mesmo no modo de teclado do laptop, que também duplica
essas funções em teclas que não são do teclado numérico.

No entanto, alguns usuários têm um teclado numérico no laptop e preferem
usá-lo para fins de navegação no Windows (pelo menos em parte do tempo),
especialmente porque alguns laptops não oferecem as teclas home, end ou
outras teclas semelhantes.  É nesse ponto que esse complemento pode ajudar.
Além disso, alguns usuários de desktop, por exemplo, aqueles acostumados com
a forma como o teclado numérico funciona no JAWS, às vezes podem achar
conveniente usar o teclado numérico para essas funções do teclado em vez das
teclas normais do NVDA, que este complemento permite.  Isso inclui o popular
comando do JAWS NumpadInsert+Numpad2, para leitura até o fim, que foi uma
solicitação de recurso específica de alguns dos primeiros usuários desse
complemento.

### Como funciona

Com o numlock desativado, independentemente do layout de teclado que estiver
usando, esse complemento permitirá que você pressione Alt+NVDA+NumpadPlus
(que geralmente é a segunda tecla longa à direita) para alternar rápida e
facilmente entre os controles de navegação normais do NVDA e os controles de
navegação clássicos do Windows. Essa tecla pode ser remapeada em Gestos de
entrada, na seção Entrada.

Note que esse complemento não desativa o uso da inserção do teclado numérico
como modificador do NVDA, se você o tiver configurado como tal. Se desejar
esse recurso, informe-me, embora você possa desativar manualmente a inserção
do teclado numérico como modificador nas configurações de teclado do
NVDA. Isso também não altera a função NVDA de exclusão do teclado numérico
(tecla entre zero e enter) - entre em contato comigo se desejar isso.

Se preferir que o NVDA inicie com o modo de navegação do Windows ativo por
padrão, você pode definir isso na configuração do NVDA.  Vá para as
preferências do NVDA, depois para as configurações e encontre o painel de
configurações do Modo de navegação do Teclado numérico.  Lá, você poderá
marcar uma caixa de seleção para ativar o modo de navegação do Windows por
padrão ao iniciar o NVDA.  Para chegar lá rapidamente, pressione NVDA+N, P,
S e, em seguida, N uma ou mais vezes até ouvir “Numpad Nav Mode”.

### Recursos do Numlock

Por padrão, nada é feito com a tecla numlock.

No entanto, se você compartilha o computador com um usuário com visão que
prefere que o numlock esteja sempre ativado, mas você gosta de desativá-lo
para que o teclado numérico funcione com o NVDA, talvez queira que o numlock
seja desativado automaticamente quando o NVDA for iniciado.  Como
alternativa, você pode inserir muitos dados e preferir que o numlock esteja
sempre ligado quando iniciar o NVDA.

 Vá para o menu NVDA, Preferências, Configurações, Modo de navegação do teclado numérico e use o seletor “estado do teclado numérico quando o NVDA é iniciado ou o perfil é carregado”. Ele tem três opções. A primeira, “não alterar", é o padrão e não mexerá no teclado numérico. Ele estará no estado em que se encontrava antes do início do NVDA.
A segunda opção é “desativar o numlock", que sempre desativará o numlock quando o NVDA for iniciado. A terceira opção, “Ativar o numlock", ativará o numlock se ele estiver desativado quando o NVDA for iniciado.
Se você escolher a segunda ou a terceira opção, o numlock será restaurado para o estado em que estava antes, quando você sair do NVDA. Por exemplo, se você escolher “Desativar o numlock" e o numlock estava ativado quando você iniciou o NVDA, ele será desativado enquanto você estiver usando o NVDA, mas será ativado novamente quando você sair do NVDA.

#### Casos de uso avançados

Se você usar os perfis de configuração avançados do NVDA e quiser que o
teclado numérico seja ativado automaticamente quando você entrar em
determinados perfis, faça o seguinte:

* Enquanto estiver no “perfil normal”, vá para o painel de configurações do
  modo de navegação do Teclado Numérico descrito acima. Marque a caixa de
  seleção “O estado inicial do teclado numérico depende do perfil de
  configuração". Essa opção está desmarcada por padrão.
* Selecione OK.
* Mude para o perfil em que você deseja que o numlock esteja sempre ativado
  ou desativado.
* Volte ao painel de configurações do Modo de navegação do teclado numérico
  e selecione a opção Ativar ou desativar o teclado numérico, conforme sua
  preferência.
* Então, selecione OK. Agora, sempre que você entrar nesse perfil, o teclado
  numérico mudará automaticamente para o estado desejado.

Note que esse é um recurso novo, e não sei se alguém já o utilizou. Se você
encontrar um, envie um e-mail ou abra [uma edição][3] para que eu saiba como
você o utilizou.

Ou, melhor ainda, deixe uma [avaliação][4] para o complemento e comente
sobre ele lá! As avaliações são muito úteis, independentemente de você usar
ou não esse recurso.

### Novos recursos

Incentivo você a publicar um [issue][3] ou enviar um e-mail com sugestões de
recursos ou outros casos de uso que eu não tenha listado aqui, ou apenas
para que eu saiba que você acha o complemento útil! Mas, conforme mencionado
acima, se você achar que ele é útil, deixe uma [avaliação][4].

### Histórico

Esse complemento foi o resultado direto de solicitações que ouvi de usuários
ao longo dos anos e de uma discussão no GitHub em [#9549]
(https://github.com/nvaccess/nvda/issues/9549). Agradecimentos a
@Qchristensen e @feerrenrut.  A implementação básica dos recursos de numlock
foi emprestada do complemento legado NumLock Manager, de Noelia Ruiz
(@nvdaes no GitHub) e outros. Usado com permissão.

### Registro de alterações

(Este registro de alterações está incompleto. Consulte o registro do Git
para obter todos os detalhes.)

* 24.1.0: Compatibilidade com o NVDA 2024.X.
* 23.1.0: Adicionados recursos de gerenciamento de numlock. Melhor registro
  em log. Manuseio aprimorado do perfil de configuração (WIP).
* 23.0: Compatibilidade com o NVDA 2023.X.

[[!tag dev stable]]

[1]: https://www.nvaccess.org/addonStore/legacy?file=numpadNavMode

[2]: https://nvaccess.org/

[3]: https://github.com/opensourcesys/numpadNavMode/issues/new

[4]: https://github.com/nvaccess/addon-datastore/discussions/2630
