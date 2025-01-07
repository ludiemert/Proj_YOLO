import cv2
import numpy as np

video = cv2.VideoCapture('dog1.mp4') #caminho da img, se for fazer online trocar por camera 0 ou 1  a camera que vc tem
classes = [] #variavel, vao conter todas as classes do coco.names

#abre o arquivo coco.names, se[ara linha por linha, e guardamos dentro da variavel classes
with open('coco.names','rt') as arquivo:
    classes = arquivo.read().rstrip('\n').split('\n')

#caminho, rodando com tiny com acuracia menor
#modeloConf = 'yolov3-tiny.cfg' #arquivo de configuracao
#modeloWeights = 'yolov3-tiny.weights' #arquivo de peso
#confThresh = 0.5 #confianca de 50% da img

#caminho, rodando com yolov3 com acuracia maior, img 320x320
modeloConf = 'yolov3.cfg' #arquivo de configuracao
modeloWeights = 'yolov3.weights' #arquivo de peso
confThresh = 0.5 #confianca de 50% da img

#configuracoes da rede
net = cv2.dnn.readNetFromDarknet(modeloConf,modeloWeights)
net.setPreferableBackend(cv2.dnn.DNN_BACKEND_OPENCV) #back end
net.setPreferableTarget(cv2.dnn.DNN_TARGET_CPU) #para rodar na cpu

#looping infinito
while True:
    check,img = video.read() #leitura da img
    img = cv2.resize(img,(1090,720)) #resolucao do video
    blob = cv2.dnn.blobFromImage(img,1/255,(320,320),[0,0,0],1,crop=False) #cria essa img
    net.setInput(blob) #define uma variavel o imput da rede
    layerNames = net.getLayerNames()
    outputNames = [layerNames[i-1] for i in net.getUnconnectedOutLayers()]
    outputs = net.forward(outputNames) #variavel de confianca
    imH, imW, imC = img.shape

    #3 arrays e 3 variaveis para conter esses dados
    bbox = []
    classIds = []
    confs = []
    for output in outputs:
        for det in output: #percorre todas as variaveis output
            scores = det[5:] #essa variavel pega apartir da posicao 5 do array, percorrendo a saida
            classId = np.argmax(scores)
            confidence = scores[classId] #limite de confianca de haver o objeto

            #definicao do trash rold de 50%, comecamos a extrair as informacoes que precisamos
            if confidence > confThresh:
                w,h = int(det[2]*imW), int(det[3]*imH) #altura e largura
                x,y = int((det[0]*imW)-w/2), int((det[1]*imH)-h/2) # e a posicao X e Y, a rede retorna na forma de proporcao
                bbox.append([x,y,w,h]) #nessa variavel adicionamos a informacao
                classIds.append(classId) # add a classe do obje identificado
                confs.append(float(confidence)) # a variavel confs adiciona o valor de confianca

    #evita poluicao na imagem
    indices = cv2.dnn.NMSBoxes(bbox,confs,confThresh,0.3)

    #percorre a variavel indices
    for i in indices:
        box = bbox[i]
        x,y,w,h = box[0],box[1],box[2],box[3]
        cv2.rectangle(img,(x,y),(x+w,y+h),(0,255,0),2) # retangulo na imagem
        cv2.putText(img,f'{classes[classIds[i]].upper()} {int(confs[i]*100)}%',(x,y-10),
                    cv2.FONT_HERSHEY_SIMPLEX,0.5,(0,0,255),2) # texto na img com classe identifi e o limite de confianca

    cv2.imshow('Video',img)
    cv2.waitKey(1)

    # Yolo rodando no CPU 320 x 320