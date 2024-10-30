# Detector de Like e Deslike para TV Corporativa

Este projeto foi desenvolvido como um estudo experimental para implementação de um sistema de interação com TV corporativa. O objetivo é permitir que colaboradores possam expressar reações em tempo real ao conteúdo exibido (como "Like" e "Deslike") utilizando gestos manuais detectados pela câmera. O sistema usa **Python**, **OpenCV** e **MediaPipe** para capturar e interpretar gestos, proporcionando uma experiência de interação simples e sem necessidade de dispositivos físicos adicionais.

## Funcionalidades

- **Detecção de Gestos**: Identifica a mão do usuário e detecta gestos de "Like" (polegar para cima) e "Deslike" (polegar para baixo).
- **Feedback Visual**: Exibe mensagens na tela indicando o gesto detectado.
- **Interação em Tempo Real**: Utiliza uma câmera para captura ao vivo, permitindo interação em tempo real.

## Tecnologias Utilizadas

- [Python 3](https://www.python.org/)
- [OpenCV](https://opencv.org/): Para captura de vídeo e exibição das imagens com feedback visual.
- [MediaPipe](https://google.github.io/mediapipe/): Para detecção de mãos e pontos de referência que permitem o reconhecimento dos gestos.

## Como Funciona

1. O programa captura a imagem da câmera e espelha para uma visão de selfie.
2. Usa o **MediaPipe Hands** para identificar pontos de referência da mão e acompanhar a posição dos dedos.
3. Verifica a posição do polegar e dos outros dedos para interpretar o gesto.
   - **Like**: Todos os dedos dobrados, exceto o polegar para cima.
   - **Deslike**: Todos os dedos dobrados, exceto o polegar para baixo.
4. Exibe feedback visual na tela e imprime no console.

## Como Executar

### Pré-requisitos

- Python 3.x
- Instalar as bibliotecas necessárias com o seguinte comando:

```bash
pip install opencv-python mediapipe
```

### Execução

Execute o script com o seguinte comando:

```bash
python main.py
```

A câmera será ativada automaticamente, e a janela do aplicativo exibirá o vídeo ao vivo, detectando os gestos.

## Aplicação Futuras

Este projeto serve como base para um sistema de interação para TVs corporativas onde o conteúdo exibido pode ser avaliado em tempo real. O conceito pode ser expandido para incluir outras reações ou comandos e melhorar a experiência do colaborador.

## Licença

Este é um projeto de estudo e ainda não possui uma licença específica. Sinta-se à vontade para estudar e contribuir com melhorias. 
