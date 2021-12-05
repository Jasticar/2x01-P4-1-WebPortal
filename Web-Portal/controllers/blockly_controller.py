from models.blockly import Blockly
from flask import Flask, render_template, Blueprint, jsonify, request
from models import blockly
from controllers import connection_controller

blockly_page = Blueprint('blockly_page', __name__)
block_arr = []
obj = Blockly()

def get_instructions():
    instruction = block_arr
    return instruction



@blockly_page.route('/blockly', methods=['GET', 'POST'])
def blocklyPage():
    if request.method == 'POST':
        data = request.get_json()
        obj.set_instructions(get_instructions(data['instructions']))
        connection_controller.send_instruction(obj)
        result = {'processed': 'true'}
        return jsonify(result)

    return render_template('blockly.html', data=get_instructions())

