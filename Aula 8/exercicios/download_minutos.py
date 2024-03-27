tamanho_arquivo = float(input("Quantos mb tem o arquivo? "))
velocidade_link = float(input("Qual o Mbps? "))

tamanho_bytes = tamanho_arquivo * 1000 * 1000
velocidade_bytes = velocidade_link * 1000 * 1000 / 8
seg_velocidade_download = tamanho_bytes / velocidade_bytes
velocidade_minuto = seg_velocidade_download / 60
print("tempo_donlownd ",  velocidade_minuto, " minutos")
