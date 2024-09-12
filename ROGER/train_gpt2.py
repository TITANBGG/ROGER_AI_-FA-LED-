import torch
from transformers import GPT2Tokenizer, GPT2LMHeadModel, Trainer, TrainingArguments, DataCollatorForLanguageModeling
from datasets import load_dataset

# GPU'nun mevcut olup olmadığını kontrol edelim
device = 'cuda' if torch.cuda.is_available() else 'cpu'

# GPT2 tokenizer'ı yükleyelim
tokenizer = GPT2Tokenizer.from_pretrained("gpt2")
tokenizer.pad_token = tokenizer.eos_token  # EOS token'ı pad token olarak kullanıyoruz.

# IMDb veri setini yükleyelim
dataset = load_dataset("imdb")

# Tokenizasyon fonksiyonu
def tokenize_function(examples):
    tokens = tokenizer(examples['text'], padding="max_length", truncation=True, max_length=512)
    tokens["labels"] = tokens["input_ids"].copy()  # Labels olarak input_ids'leri kullanıyoruz
    return tokens

# IMDb veri setini tokenize edelim
tokenized_imdb = dataset['train'].map(tokenize_function, batched=True)

# GPT2 modelini ve tokenizer'ını yükleyelim
model = GPT2LMHeadModel.from_pretrained("gpt2")
model = model.to(device)

# Veri toplama işlemi için padding ve maskalama işlemi
data_collator = DataCollatorForLanguageModeling(tokenizer=tokenizer, mlm=False)

# Modeli eğitme için ayarları yapalım
training_args = TrainingArguments(
    output_dir="./results",
    evaluation_strategy="epoch",
    num_train_epochs=1,
    per_device_train_batch_size=4,
    save_steps=10_000,
    save_total_limit=2,
)

# Trainer ile modeli eğitelim
trainer = Trainer(
    model=model,
    args=training_args,
    train_dataset=tokenized_imdb,
    data_collator=data_collator
)

trainer.train()
