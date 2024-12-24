import streamlit as st
import random
import string

# Titre et description
st.title("🔑 Générateur de mots de passe")
st.write("Créez des mots de passe sécurisés en quelques clics. Personnalisez la longueur selon vos besoins !")

# Paramètres utilisateur
length = st.slider("Choisissez la longueur du mot de passe :", 8, 32, 12)

# Génération de mot de passe
if st.button("Générer un mot de passe"):
    characters = string.ascii_letters + string.digits + string.punctuation
    password = ''.join(random.choice(characters) for _ in range(length))
    st.success(f"💡 Mot de passe généré : {password}")
else:
    st.info("Cliquez sur le bouton pour générer un mot de passe.")

# Footer
st.write("💻 Projet réalisé avec Python. Pour voir le code source, [cliquez ici](https://github.com/tonpseudo/projet).")
