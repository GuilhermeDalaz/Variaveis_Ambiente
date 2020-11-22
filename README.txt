#Tutorial:

1- Primeiramente deve-se instalar alguns arquivos atráves do pip, para isto basta digitar o seguinte comando no seu prompt:
pip install -r requirements.txt

2- Agora devemos setar as váriaveis de ambiente pelos comandos:
Publish key: set pubsub_pub=pub-c-c9e508a4-19cb-4c87-b412-c5fa7999accb
Subscribe key: set pubsub_sub=sub-c-7760a76-069b-11eb-a4c5-6ea1d8be3fc3

3- Então abra 2 terminais e execute os dois comandos abaixo, cada um em um terminal diferente:
python chat-enviar.py
python chat-receber.py
