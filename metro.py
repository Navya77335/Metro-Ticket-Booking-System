while True:
    ch=input('who want open the list of the metro(passenger or owner):')
    if ch=='owner':
        use='owner'
        pas='1234'
        user=input('enter user owner name:')
        password=input('enter owner pass word:')
        if use==user and pas==password:
            import mysql.connector as db
            con=db.connect(user='root',password='p.navi77',host='localhost',
                       database='metro_ticket')
            cur=con.cursor()
            cur.execute('select * from r')
            r=cur.fetchall()
            print('\n')
            print(15*'*','Red Line Stations','*'*15,'\n')

            print(f"{'-:Station_Name:-':<25}{'-:Distance For Km:-':<30}{'-:Charges:-':<25}")
            for row in r:
                print(f"{row[0]:<30}{row[1]:<30}{row[2]:<30}")
            cur.execute('select * from b')
            b=cur.fetchall()
            print('\n')
            print(15*'*','Blue Line Stations','*'*15,'\n')

            print(f"{'-:Station_Name:-':25}{'-:Distance For Km:-':<30}{'-:charges:-':<25}")
            for t in b:
                print(f"{t[0]:<30}{t[1]:<30}{t[2]:<30}")
            cur.execute('select * from gr')
            g=cur.fetchall()
            print(15*'*','Green Line Station','*'*15,'\n')
            print(f"{'-:Station_Name:-':<25}{'-:Distance For Km:-':30}{'-:charges:-':<25}")
            for n in g:
                print(f"{n[0]:<30}{n[1]:<30}{n[2]:<30}")
            cur.execute('select * from booking_table')
            res=cur.fetchall()
            print(f"{'-:name:-':<15}{'-:age:-':<15}{'-:gender:-':<15}{'-:from:-':<15}{'-:to:-':<15}")
            for l in res:
                print(f"{l[0]:<15}{l[1]:<15}{l[2]:<15}{l[3]:<15}{l[4]:<15}")
            cur.close()
            con.close()

        else:
            print('enter correct user and password')
            break
    else:
        print('1.bocking your ticket')
        print('2.cancle your ticket')
        print('3.display')
        print('4.Exit')
        ch=int(input('enter your choice:'))
        if ch==1:
            import mysql.connector as db
            name=input('enter your name:')
            age=int(input('enter your age:'))
            gender=input('enter your gender:')
            from_station=input('enter where your are start:')
            to_station=input('enter where your reach:')
            con=db.connect(user='root',password='p.navi77',host='localhost',
                               database='metro_ticket')
            cur=con.cursor()
            cur.execute('select fare from r where station_name=%s',(from_station,))
            res=cur.fetchone()
            fare_r=res[0]if res else None
            cur.execute('select fare from b where station_name=%s',(from_station,))
            res=cur.fetchone()
            fare_b=res[0]if res else None
            cur.execute('select fare from gr where station_name=%s',(from_station,))
            res=cur.fetchone()
            fare_gr=res[0]if res else None

            fare_from=fare_r or fare_b or fare_gr

            cur.execute('select fare from r where station_name=%s',(to_station,))
            res=cur.fetchone()
            fare_red=res[0]if res else None
            cur.execute('select fare from b where station_name=%s',(to_station,))
            res=cur.fetchone()
            fare_blue=res[0]if res else None
            cur.execute('select fare from gr where station_name=%s',(to_station,))
            res=cur.fetchone()
            fare_green=res[0]if res else None
            fare_to=fare_red or fare_blue or fare_green
            if fare_from is not None and fare_to is not None:
                print('Name of the passneger:',name)
                amount=abs(fare_to-fare_from)
                cur.execute('select id from booking_table')
                res=cur.fetchone()
                for i in res:
                    print('RGID:',i)
                if gender=='female' and age>60:
                    discount=amount*0.25
                    print('discount for yelder ladies:',discount)
                    res=amount-discount
                    print('you can pay:',res)
                elif gender=='male' and age>60:
                    discount=amount*0.15
                    print('discount for yelder mans:',discount)
                    res=amount-discount
                    print('you can pay:',res)
                elif gender=='female':
                    discount=amount*0.10
                    print('discount for ladies:',discount)
                    res=amount-discount
                    print('you can pay:',res)
                elif gender=='transe':
                    print('do not pay the amount')
                else:
                    print('please enter correct gender')
                if('select * from r')!=('select * from b')!=('select * from gr'):
                    print('you can change the line')
                con=db.connect(user='root',password='p.navi77',host='localhost',
                               database='metro_ticket')
                cur=con.cursor()
                cur.execute('insert into booking_table(passenger_name,age,gender,from_station,to_station)values(%s,%s,%s,%s,%s)',(name,age,gender,from_station,to_station))
                con.commit()
                print('ticket is booking successfully')
            else:
                print('please enter valid data')
            cur.close()
            con.close()
        if ch==2:
            import mysql.connector as db
            con=db.connect(user='root',password='p.navi77',host='localhost',
                           database='metro_ticket')
            cur=con.cursor()
            name=input('enter name of the passenger:')
            age=int(input('enter age of the passenger:'))
            gender=input('enter gender of the passenger:')
            cur.execute('SELECT COUNT(*) FROM booking_table WHERE passenger_name=%s AND age=%s AND gender=%s', (name, age, gender))
            record_exists = cur.fetchone()[0]

            if record_exists:
                cur.execute('delete from booking_table where passenger_name=%s and age=%s and gender=%s',(name,age,gender))
                con.commit()
                print('ticket_booking is successfully cancelled')
            else:
                print('please enter valid data')
            cur.close()
            con.close()
        elif ch==3:
            import mysql.connector as db
            con=db.connect(user='root',password='p.navi77',host='localhost',
                           database='metro_ticket')
            cur=con.cursor()
            cur.execute('select * from r')
            r=cur.fetchall()
            print('\n')
            print(15*'*','Red Line Stations','*'*15,'\n')

            print(f"{'-:Station_Name:-':<25}{'-:Distance For Km:-':<30}{'-:Charges:-':<25}")
            for row in r:
                print(f"{row[0]:<30}{row[1]:<30}{row[2]:<30}")
            cur.execute('select * from b')
            b=cur.fetchall()
            print('\n')
            print(15*'*','Blue Line Stations','*'*15,'\n')

            print(f"{'-:Station_Name:-':25}{'-:Distance For Km:-':<30}{'-:charges:-':<25}")
            for t in b:
                print(f"{t[0]:<30}{t[1]:<30}{t[2]:<30}")
            cur.execute('select * from gr')
            g=cur.fetchall()
            print(15*'*','Green Line Station','*'*15,'\n')
            print(f"{'-:Station_Name:-':<25}{'-:Distance For Km:-':30}{'-:charges:-':<25}")
            for n in g:
                print(f"{n[0]:<30}{n[1]:<30}{n[2]:<30}")
            cur.close()
            con.close()
        elif ch==4:
            print('pani ipoendhi ga pani chusuko po ekka ')
            break


    
        
            
    
