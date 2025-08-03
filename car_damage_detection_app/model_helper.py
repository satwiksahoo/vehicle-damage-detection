from PIL import Image
import torch , torchvision
from torch import nn
from torchvision import models , transforms

trained_model = None
class_names = ['Front Breakage', 'Front Crushed', 'Front Normal', 'Rear Breakage', 'Rear Crushed', 'Rear Normal']
class CarClassifierResNet(nn.Module):
    def __init__(self , num_classes):
        super().__init__()
        self.model = models.resnet50(weights = 'DEFAULT')
        
        # in_features = self.model.classifier[1].in_features
        
        for param in self.model.parameters():
            param.requires_grad = False

        for param in self.model.layer4.parameters():
            param.requires_grad = True
            
        self.model.classifier = nn.Sequential(
          
            # nn.Linear(in_features , 512) , 
            
            # nn.ReLU() , 
            # nn.Dropout(p =0.2) ,

            # nn.Linear(512 , 128) ,
            # nn.ReLU() ,
            # nn.Dropout(p = 0.2) ,
            nn.Dropout(p = 0.6),


            nn.Linear(self.model.fc.in_features , num_classes)
            
        

        


           
        

            
            
        )
    def forward(self ,x):
        y = self.model(x)
        return y 

def predict(image_path):
    image = Image.open(image_path).convert('RGB')
    
    transform = transforms.Compose([

    transforms.Resize((224,224)),
    transforms.ToTensor(),
    transforms.Normalize((0.485 , 0.456 , 0.406) , (0.229  ,0.224 , 0.225))

    
])
    image_tensor = transform(image).unsqueeze(0)
    
    global trained_model
    
    if not trained_model:
        trained_model = CarClassifierResNet(len(class_names))
    
        trained_model.load_state_dict(torch.load('model/saved_model.pth'))
    
        trained_model.eval()
        
        
    
    
    with torch.no_grad():
        output = trained_model(image_tensor)
        
        _ , predicted_class = torch.max(output , 1)
        
        
        return class_names[predicted_class.item()]
        
        
    
    
    
 
    
    
    