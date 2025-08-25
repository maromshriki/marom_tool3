marom_tool4 – CLI לניהול משאבים ב־AWS

כלי שורת פקודה (CLI) פשוט ב־Python לניהול משאבי AWS:
EC2, ‏S3, ‏Route53.
הכלי נבנה לעבודה עם region us-east-1 בלבד, כולל פלט נקי וברור.


הורד git 
    sudo yum install git -y
    
וודא שיש לך Python 3.9+ מותקן.
הורד את הrepo 
git clone https://github.com/maromshriki/marom_tool3.git

חשבון AWS עם הרשאות מתאימות (EC2, S3, Route53)
aws configure והשלמת כל הנתונים שלך

התקן את התלויות והכן את הסביבה תן הרשאות לקובץ marom.sh והרץ אותו:
chmod +x marom.sh
./marom.sh

הגדר הרשאות AWS (באמצעות aws configure או environment variables).

 שימוש

הפקודה הכללית:

python3 cli.py <resource> <action> [options...]


יצירת instance חדש
python3 cli.py ec2 create --type t2.micro --os ubuntu


 ייווצר instance עם Public IP ו־Tag CreatedBy=marom_tool2.

פלט לדוגמה:


Instance created ID: i-0123456789abcdef0

הצגת כל ה־instances
python3 cli.py ec2 describe


פלט לדוגמה:

=== EC2 Instances ===
- i-0123456789abcdef0 | t2.micro | running | Public IP: 54.12.34.56

מחיקת instance
python3 cli.py ec2 terminate --id i-0123456789abcdef0


פלט:




יצירת bucket
python3 cli.py s3 create --name my-bucket

הצגת כל ה־buckets
python3 cli.py s3 list

מחיקת bucket
python3 cli.py s3 delete --name my-bucket

העלאת קובץ ל־S3
python3 cli.py s3 upload --bucket my-bucket --file /path/to/file.txt
# יצירת באקט
python3 cli.py s3 create --name marom-bucket-test

# העלאת קובץ
python3 cli.py s3 upload --bucket marom-bucket-test --file ./document.txt

# הצגת הקבצים בבאקט
python3 cli.py s3 list --bucket marom-bucket-test

# מחיקת קובץ
python3 cli.py s3 delete --bucket marom-bucket-test --file document.txt



אפשר גם להגדיר שם ייחודי לאובייקט:

python3 cli.py s3 upload --bucket my-bucket --file /path/to/file.txt --key newname.txt

 Route53
יצירת Hosted Zone
python3 cli.py route53 create --domain example.com

הצגת כל ה־zones
python3 cli.py route53 list

מחיקת Hosted Zone
python3 cli.py route53 delete --id Z1234567890



Python 3.9+

boto3


