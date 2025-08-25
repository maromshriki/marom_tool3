# marom_tool2

כלי CLI פשוט ליצירת וניהול משאבים ב-AWS (S3, EC2, Route53) באזור us-east-1 בלבד.

## התקנה
```bash
pip install -r requirements.txt
```

## שימוש
### S3
- יצירת bucket:
```bash
python cli.py s3 create --name my-bucket
```
- העלאת קובץ:
```bash
python cli.py s3 upload --bucket my-bucket --file ./local.txt --key remote.txt
```
- מחיקת קובץ:
```bash
python cli.py s3 delete-file --bucket my-bucket --key remote.txt
```
- מחיקת bucket:
```bash
python cli.py s3 delete --name my-bucket
```

### EC2
- יצירת מכונה:
```bash
python cli.py ec2 create --type t2.micro --os ubuntu
```
- עצירה/הפעלה/מחיקה:
```bash
python cli.py ec2 stop --id i-123456
python cli.py ec2 start --id i-123456
python cli.py ec2 terminate --id i-123456
```

### Route53
- יצירת hosted zone:
```bash
python cli.py route53 create-zone --name example.com
```
- יצירת רשומה:
```bash
python cli.py route53 create-record --zone-id ZONEID --name test.example.com --type A --value 1.2.3.4
```
- מחיקת רשומה:
```bash
python cli.py route53 delete-record --zone-id ZONEID --name test.example.com --type A --value 1.2.3.4
```
