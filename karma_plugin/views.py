from flask import Blueprint, render_template, abort
from karma_plugin import KarmaPlugin
from marvinbot.utils import localized_date

karma_app = Blueprint('karma', __name__, template_folder='templates')

@karma_app.route('/', methods=['GET'])
def karmareport_global():
    date = localized_date()
    return render_template('karmareport.html', title='Global', report=KarmaPlugin.get_karma_report(), date=date)

@karma_app.route('/<chat_id>', methods=['GET'])
def karmareport(chat_id):
    try:
        chat = getattr(karma_app, 'adapter').bot.getChat(chat_id)
    except:
        # Render 404 Not Found page
        abort(404)
        return
    date = localized_date()
    return render_template('karmareport.html', title=chat.title, report=KarmaPlugin.get_karma_report(int(chat_id)), date=date)
