from flask import render_template, flash, redirect, url_for, request, session
from app import app
from app.forms import TwitInfoForm, InstaInfoForm, ModalForm
from app import user_info, insta_info
import babel


@app.route('/')
def index():
    return render_template('base.html')

@app.route('/instainfo', methods=['GET','POST'])
def instainfo():
    form = InstaInfoForm()
    session['instauser'] = form.username.data
    session['password'] = form.password.data
    if form.validate_on_submit():
        
        return redirect(url_for('successinsta'))
    return render_template('instainfo.html', form=form)

@app.route('/successinsta', methods=['GET','POST'])
def successinsta():
    names = []
    user = session['instauser']
    pw = session['password']
    api = insta_info.createAPI(user, pw)
    
    if (api.login()):
        names = insta_info.getNotFollowing(api, api.username_id)
        followers = insta_info.getTotalFollowers(api, api.username_id)
        following = insta_info.getTotalFollowing(api, api.username_id)
        return render_template('success-insta.html', names=names, length=len(names), user=user, followers=len(followers), following=len(following))
    else:
        if(api.LastJson['error_type'] == 'bad_password'):
            form = InstaInfoForm()
            flash('The username/password you have entered is incorrect.', 'error')
            return render_template('instainfo.html', form=form)
        else:
            return render_template('instainfo.html', form=form)
        """         if(api.LastJson['message'] == 'challenge_required'):
            path = api.LastJson['challenge']['api_path'][1:]
            session['path'] = path
            choice = 0 # 0 - SMS; 1 - EMail
            api.getCodeChallengeRequired(path, choice)
            #code = input('Enter the code: ')
            #api.setCodeChallengeRequired(path,code)
            return redirect(url_for('captchaform')) """
    
#Amtulskitchenn

@app.route('/captchaform', methods=['GET', 'POST'])
def captchaform():
    form = ModalForm()
    oldForm = InstaInfoForm()
    user = session['instauser']
    pw = session['password']
    api = insta_info.createAPI(user,pw)
    if form.validate_on_submit():
        session['code'] = form.code
        return redirect(url_for('captchacode'))
    return render_template('code.html', form=form, oldForm= oldForm)

@app.route('/captcha', methods=['GET','POST'])
def captchacode():
    user = session['instauser']
    pw = session['password']
    api = insta_info.createAPI(user,pw)
    code = session['code']
    api.setCodeChallengeRequired(session['path'],code)
    if(api.login()):
        names = insta_info.getNotFollowing(api, api.username_id)
        followers = insta_info.getTotalFollowers(api, api.username_id)
        following = insta_info.getTotalFollowing(api, api.username_id)
        return render_template('success-insta.html', names=names, length=len(names), user=user, followers=len(followers), following=len(following))
    else:
        return redirect(url_for('instainfo'))
    

@app.route('/twitinfo', methods=['GET','POST'])
def twitinfo():
    form = TwitInfoForm()
    session['twituser'] = form.username.data
    if form.validate_on_submit():
        
        return redirect(url_for('success'))
    return render_template('index.html', title='Enter your user', form=form)


def format_datetime(value, format='medium'):
    if format == 'full':
        format="EEEE, d. MMMM y 'at' HH:mm"
    elif format == 'medium':
        format="EE dd.MM.y HH:mm"
    return babel.dates.format_datetime(value, format)
    

@app.route('/success')
def success():
    names = []
    user = session['twituser']
    if user_info.tweep.TweepError:
        form = TwitInfoForm()
        flash('The username/password you have entered is incorrect.', 'error')
        return render_template('index.html', form=form)
    else:
        account = user_info.my_api.get_user(user)
        date = format_datetime(account.created_at)
        image_url = user_info.my_api.get_user(user).profile_image_url
        diff_list = user_info.get_difference_in_followers(user) 
        for user_id in diff_list:
            names.append(user_info.my_api.get_user(user_id).screen_name)
        return render_template('success.html', names=names, length=len(diff_list), image_url=image_url, name=user, account=account, date=date)



