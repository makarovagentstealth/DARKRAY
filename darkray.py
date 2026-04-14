import os
import socket
import csv
import numpy as np
from astropy.coordinates import SkyCoord
from astropy import units as u
from gtts import gTTS
import math

class DeepGravityMapper:
    def __init__(self, target_domain):
        self.domain = target_domain
        self.ip_address = ""
        self.log_file = "gravity_exploration_report.csv"
        self.audio_file = "acoustic_pattern.mp3"

    def resolve_network(self):
        """Mapeia o domínio para IPv4."""
        try:
            self.ip_address = socket.gethostbyname(self.domain)
            print(f"[LOG] Entrelaçamento de Rede: {self.domain} -> {self.ip_address}")
            return True
        except Exception as e:
            print(f"[ERRO] Falha na conexão eletromagnética: {e}")
            return False

    def generate_astrometric_grid(self):
        """Gera pontos de hardware respeitando os limites da física astronômica."""
        # Semente baseada nos octetos do IP
        ip_parts = [int(x) for x in self.ip_address.split('.')]
        ip_sum = sum(ip_parts)
        
        # RA (Ascensão Reta) pode ser de 0 a 360 - usamos o módulo para garantir
        ra_val = ip_sum % 360
        
        # CORREÇÃO DO ERRO: Declinação (Latitude) deve ser entre -90 e 90.
        # Usamos o seno da soma dos octetos para mapear o valor para o intervalo [-1, 1]
        # e então multiplicamos por 90 para cobrir toda a amplitude permitida.
        dec_val = 90 * math.sin(math.radians(ip_sum))
        
        coord = SkyCoord(ra=ra_val*u.degree, dec=dec_val*u.degree, frame='icrs')
        
        print(f"[LOG] Coordenadas Físicas Validadas: RA:{coord.ra.value:.2f}°, DEC:{coord.dec.value:.2f}°")
        return coord

    def synthesize_acoustic_consonants(self, coord):
        """Converte os dados em padrões acústicos .mp3."""
        acoustic_data = (f"Hardware em profundidade de {coord.ra.value:.2f} graus. "
                        f"Vetor gravitacional de declinação em {coord.dec.value:.2f} graus. "
                        f"Assinatura do IP {self.ip_address} processada.")
        
        print(f"[LOG] Sintetizando consoantes acústicas...")
        tts = gTTS(text=acoustic_data, lang='pt')
        tts.save(self.audio_file)

    def save_report(self, coord):
        """Gera o relatório CSV."""
        with open(self.log_file, mode='w', newline='') as file:
            writer = csv.writer(file)
            writer.writerow(["Parametro", "Resultado", "Explicação Física"])
            writer.writerow(["Dominio", self.domain, "Alvo do mapeamento"])
            writer.writerow(["IPv4", self.ip_address, "Assinatura eletromagnética"])
            writer.writerow(["Ascensão Reta", f"{coord.ra.value:.4f}", "Profundidade na grade"])
            writer.writerow(["Declinação", f"{coord.dec.value:.4f}", "Gravidade (Normalizada)"])
            writer.writerow(["Status", "Sucesso", "Dados dentro dos limites de SkyCoord"])

    def run(self):
        print(f"--- Iniciando C2-Gravity Mapper ---")
        if self.resolve_network():
            coord = self.generate_astrometric_grid()
            self.synthesize_acoustic_consonants(coord)
            self.save_report(coord)
            print(f"--- Processo Finalizado com Sucesso ---")
            print(f"Log: {self.log_file} | Áudio: {self.audio_file}")

if __name__ == "__main__":
    target = input("Domínio alvo: ")
    mapper = DeepGravityMapper(target)
    mapper.run()
