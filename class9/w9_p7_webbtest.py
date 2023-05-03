import webbrowser

while True :
    print('0 : 전체')
    print('1 : 이미지')
    print('2 : 뉴스')
    print('3 : 동영상')
    category = int(input('Input category :'))

    if category not in  [0,1,2,3] :
        print('The end of search~~~')
        break
    else :
        sword = input('키워드 입력 : ')
       
        urlex = 'https://www.google.com/search?q='+sword
        if category == 1 :
            urlex += '&source=lnms&tbm=isch&sa=X&ved=2ahUKEwih5tiL96r-AhXJrlYBHTR1DFoQ_AUoAXoECAEQAw&biw=1920&bih=969&dpr=1'
        if category == 2 :
            urlex += '&source=lmns&tbm=nws&bih=969&biw=1920&hl=en&sa=X&ved=2ahUKEwiFtdfA96r-AhX_t1YBHYHdAa4Q_AUoAnoECAEQAg'
        if category == 3:
            urlex += '&hl=en&tbm=vid&source=lnms&sa=X&ved=2ahUKEwj61d3F96r-AhWDmlYBHSBbDYcQ_AUoA3oECAIQBQ&biw=1920&bih=969&dpr=1'
        webbrowser.open_new(urlex)
