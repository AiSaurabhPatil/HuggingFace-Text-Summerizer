from transformers import TrainingArguments, Trainer
from transformers import DataCollatorForSeq2Seq
from transformers import AutoModelForSeq2SeqLM, AutoTokenizer
from datasets import load_from_disk , load_dataset
import torch
import os 
from text_summarizer.entity import ModelTrainerConfig

class ModelTrainer:
    def __init__(self, config:ModelTrainerConfig):
        self.config = config
    

    def train(self):
        device = "cuda" if torch.cuda.is_available() else 'cpu'
        tokenizer = AutoTokenizer.from_pretrained(self.config.model_ckpt)
        model_pegasus = AutoModelForSeq2SeqLM.from_pretrained(self.config.model_ckpt).to(device)
        seq2seq_data_collator = DataCollatorForSeq2Seq(tokenizer , model=model_pegasus)

        dataset_samsum_pt = load_from_disk(self.config.data_path)

        trainer_args = TrainingArguments(
            output_dir=self.config.root_dir,
            per_device_train_batch_size=self.config.per_device_train_batch_size,
            gradient_accumulation_steps=self.config.gradient_accumulation_steps,
            evaluation_strategy=self.config.evaluation_strategy,
            save_steps=self.config.save_steps,
            eval_steps=self.config.eval_steps,
            logging_steps=self.config.logging_steps,
            num_train_epochs=self.config.num_train_epochs,
            weight_decay=self.config.weight_decay,
            warmup_steps=self.config.warmup_steps,
            per_device_eval_batch_size=self.config.per_device_eval_batch_size

            
        )

        trainer = Trainer(
            model=model_pegasus,
            args=trainer_args,
            tokenizer=tokenizer,
            data_collator=seq2seq_data_collator,
            train_dataset=dataset_samsum_pt['test'],
            eval_dataset=dataset_samsum_pt['validation'],
        )

        trainer.train()

        model_pegasus.save_pretrained(os.path.join(self.config.root_dir,'pegasus-samsum-model'))
        tokenizer.save_pretrained(os.path.join(self.config.root_dir,'tokenizer'))