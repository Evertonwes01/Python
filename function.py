def verificar_tamanho_tweet(T):
    if len(T) <= 140:
        return "TWEET"
    else:
        return "MUTE"

# Entrada
T = input()

# Saída
print(verificar_tamanho_tweet(T))
