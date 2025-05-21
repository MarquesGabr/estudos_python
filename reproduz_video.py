import cv2
import pygame
import os

def reproduzir_video(caminho):
    video_path = os.path.join("assets", "videos", caminho)

    if not os.path.exists(video_path):
        print(f"Vídeo não encontrado: {video_path}")
        return

    cap = cv2.VideoCapture(video_path)
    if not cap.isOpened():
        print("Erro ao abrir o vídeo.")
        return

    # Captura as dimensões do vídeo
    largura = int(cap.get(cv2.CAP_PROP_FRAME_WIDTH))
    altura = int(cap.get(cv2.CAP_PROP_FRAME_HEIGHT))
    fps = cap.get(cv2.CAP_PROP_FPS)

    # Redimensiona a tela do Pygame para o tamanho do vídeo
    tela_video = pygame.display.set_mode((largura, altura))

    clock = pygame.time.Clock()
    rodando = True
    while rodando and cap.isOpened():
        ret, frame = cap.read()
        if not ret:
            break

        for evento in pygame.event.get():
            if evento.type == pygame.QUIT:
                rodando = False
                break
            if evento.type == pygame.KEYDOWN and evento.key == pygame.K_ESCAPE:
                rodando = False
                break

        # Converte o frame do OpenCV (BGR) para RGB e depois para Surface do Pygame
        frame_rgb = cv2.cvtColor(frame, cv2.COLOR_BGR2RGB)
        frame_surface = pygame.surfarray.make_surface(frame_rgb.swapaxes(0, 1))
        tela_video.blit(frame_surface, (0, 0))
        pygame.display.update()

        clock.tick(fps)

    cap.release()
