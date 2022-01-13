from kochat.data import Dataset
from kochat.loss import CRFLoss, CosFace, CenterLoss, COCOLoss, CrossEntropyLoss
from kochat.model import intent, embed, entity
from kochat.proc import DistanceClassifier, GensimEmbedder, EntityRecognizer, SoftmaxClassifier

# prepare dataset
dataset = Dataset(ood=False)

# 1. 임베딩 프로세서
emb = GensimEmbedder(model=embed.FastText())
emb.fit(dataset.load_embed()) # 모델 학습

# 3. 엔티티 검출기
rcn = EntityRecognizer(
    model=entity.LSTM(dataset.entity_dict),
    loss=CRFLoss(dataset.entity_dict)
)
rcn.fit(dataset.load_entity(emb)) # 모델 학습

# 2. 인텐트 분류기
clf = DistanceClassifier(
    model=intent.CNN(dataset.intent_dict),
    loss=CenterLoss(dataset.intent_dict),
)
clf.fit(dataset.load_intent(emb)) # 모델 학습


# 모델 학습이 완료되면 saved라는 폴더가 자동 생성되어 결과가 저장됩니다.