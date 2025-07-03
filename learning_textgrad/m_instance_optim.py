from textgrad.engine import get_engine
from textgrad import Variable
from textgrad.optimizer import TextualGradientDescent
from textgrad.loss import TextLoss
from dotenv import load_dotenv
load_dotenv()

x = Variable("A sntence with a typo", role_description="The input sentence", requires_grad=True)
# x.gradients

engine = get_engine("gpt-3.5-turbo")

engine.generate("Hello how are you?")
