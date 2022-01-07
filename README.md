
![Logo](https://dashboard.snapcraft.io/site_media/appmedia/2020/05/icon_sjsbj5P.png)

<p align="center">
  <img width="100" height="100" src="https://dashboard.snapcraft.io/site_media/appmedia/2020/05/icon_sjsbj5P.png">
</p>

# Shamsi Todo list maker

using Todo list for managing your task during a week/month is very important. with this project i trying to make a Todo-list maker program with Shamsi Date.



## Deployment

To deploy this project Follow Instructions:

* First Clone code with this:
```bash
git clone https://github.com/mertz1999/shamsi-Todo.git
```

* insert new record:

```bash
python todo.py --insert --date SHORT-DATE
```
Note: you need to use this SHORT-DATE for this Instructions:

| Date | Short-DATE     | Example                |
| :-------- | :------- | :------------------------- |
| `Farvardin` | `fa` | 12fa |
| `Ordibehesht` | `or` | 2or |
| `Khordad` | `kh` | 5kh |
| `Thir` | `ti` | 25ti |
| `Mordad` | `mo` | 10mo |
| `Shahrivar` | `sh` | 24sh |
| `Mehr` | `me` | 15me |
| `Aban` | `ab` | 1ab |
| `Azar` | `az` | 12az |
| `Dey` | `de` | 2de |
| `Bahman` | `ba` | 12ba |
| `Esfand` | `es` | 12es |

* See Todo list for a certain date:
```bash
python todo.py --write --date SHORT-DATE
```
After Running this, you can see you todo list in ./todo Folder

* See Todo list for Today:
```bash
python todo.py --today
```



## Feedback

If you have any feedback, please reach out to us at reza.tz780210@gmail.com
- [Reza Tanakizadeh](https://github.com/mertz1999)


## License

[MIT](https://choosealicense.com/licenses/mit/)

