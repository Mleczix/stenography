from PIL import Image
import os
from stegano import lsb

# Funkcja do ukrywania tekstu w obrazie
def hide_text_in_image(input_image_path, output_image_path, secret_text):
    try:
        secret_image = lsb.hide(input_image_path, secret_text)
        secret_image.save(output_image_path)
        print(f"Tekst został ukryty w obrazie i zapisany jako {output_image_path}")
        print("Ukryty tekst:", secret_text)

    except FileNotFoundError:
        print("Plik źródłowy obrazka nie istnieje.")
    except Exception as e:
        print(f"Błąd podczas ukrywania tekstu w obrazie: {e}")


# Funkcja do odkrywania tekstu z obrazu
def reveal_text_from_image(input_image_path):
    try:
        secret_image = Image.open(input_image_path)
        secret_text = lsb.reveal(secret_image)
        print("Odkryto tekst z obrazu:", secret_text)
        return secret_text
    except FileNotFoundError:
        print("Plik obrazka do odczytu nie istnieje.")
    except Exception as e:
        print(f"Błąd podczas odczytywania ukrytego tekstu z obrazu: {e}")


# Funkcja do ukrywania tekstu w tekście
def hide_text_in_text_file(original_text_path, secret_text_path, output_text_path):
    try:
        # Odczytaj oryginalny tekst z pliku
        with open(original_text_path, 'r') as file:
            original_text = file.read()

        # Odczytaj tekst, który chcesz ukryć z pliku
        with open(secret_text_path, 'r') as file:
            secret_text = file.read()

        # Zamień spację na znak specjalny (np. '/')
        original_text = original_text.replace(' ', '/')

        # Dołącz ukryty tekst do tekstu oryginalnego
        steganographic_text = original_text + ' ' + secret_text

        # Zapisz ukryty tekst do pliku wyjściowego
        with open(output_text_path, 'w') as file:
            file.write(steganographic_text)

        print(f"Ukryty tekst został zapisany jako {output_text_path}")
        print("Ukryty tekst:", steganographic_text)
    except FileNotFoundError:
        print("Plik źródłowy tekstu nie istnieje.")
    except Exception as e:
        print("Błąd podczas ukrywania tekstu w tekście:", e)


# Funkcja do odkrywania tekstu z tekstu
def reveal_text_from_text(steganographic_text):
    # Podziel tekst na części, wykorzystując spację jako separator
    parts = steganographic_text.split(' ')

    if len(parts) > 1:
        # Odkryj ukryty tekst
        secret_text = parts[1]
        print("Odkryto ukryty tekst z tekstu:", secret_text)
        return secret_text
    else:
        print("Brak ukrytego tekstu.")
        return "Brak ukrytego tekstu."

# Przykład użycia
if __name__ == "__main__":
    # Ukrywanie tekstu w obrazie
    hide_text_in_image("pythone/Obrazek.png", "pythone/output_image.png", "Testowy_tekst")

    # Odkrywanie ukrytego tekstu z obrazu
    recovered_text1 = reveal_text_from_image("pythone/output_image.png")
    print("Odkryty tekst z obrazu:", recovered_text1)

    hide_text_in_text_file("pythone/input.txt", "pythone/secret.txt", "pythone/output.txt")

    # Odczytywanie ukrytego tekstu z tekstu
    with open("pythone/output.txt", 'r') as file:
        steganographic_text = file.read()
        recovered_text = reveal_text_from_text(steganographic_text)
        print("Odkryty tekst z tekstu:", recovered_text)
