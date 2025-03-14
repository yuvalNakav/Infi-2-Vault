# הגדרות 

## 1 . טור טיילור 
 תהא $f:\left[x_{0}-\delta,x_{0}+\delta\right]\rightarrow\mathbb{R}$ המוגדרת בסביבה מלאה של $x_{0}$ וגזירה בה אינסוף פעמים. 
 נגדיר את **טור טיילור של $f$ סביב $x_{0}$** ע״י **: $$
 \begin{align*} T_{f,x_{0}}\left(x\right)=\sum_{k=0}^{\infty}\frac{f^{\left(k\right)}\left(x\right)}{k!}\left(x-x_{0}\right)^{k} \end{align*} $$ 
 לכן, לכל $x_{1}\in\mathbb{R}$ הסכום החלקי ה- $-n$ י, $S_{n}\left(x_{1}\right)$ של הטור $T_{f,x_{0}}$ הוא הערך בנקודה $x$ של פולינום טיילור מסדר $n$ של $f$ סביב $x_{0}$ : $$
 \begin{align*} S_{n}\left(x_{1}\right)=\sum_{k=1}^{n}\frac{f^{\left(k\right)}\left(x_{1}\right)}{k!}\left(x-x_{0}\right)^{k}=P_{n,f,x_{0}}\left(x_{1}\right) \end{align*} $$
## 2 . טור חזקות 
 תהא $\left(a_{k}\right)_{k=0}^{\infty}$ סדרה ב $\mathbb{R}$ , ו $x_{0}\in\mathbb{R}$ . הטור $\overset{\infty}{\underset{k=0}{\sum}}a_{k}\left(x-x_{0}\right)^{k}$ נקרא **טור חזקות (ב- $x$ ) סביב** $x_{0}$. 
 נשים לב שטור חזקות הוא טור של פונקציות, והצבת $x$ ים שונים תוליד טורים מספריים שונים. 
## 3 . תחום התכנסות 
 נגדיר את הקבוצה $\mathbb{R}\supseteq D=\left\{ x\in\mathbb{R}\mid\exists L\in\mathbb{R}\,\overset{\infty}{\underset{k=0}{\sum}}a_{k}\left(x-x_{0}\right)^{k}=L\right\}$ , **קבוצת כל ה $x$ ים הממשיים שהטור המוגדר בעזרת הסדרה $a_{k}\left(x-x_{0}\right)^{k}$ סביב $x_{0}$ מתכנס** . 
 נקרא ל $D$ **תחום ההתכנסות של $\overset{\infty}{\underset{k=0}{\sum}}a_{k}\left(x-x_{0}\right)^{k}$ . 
 נשים לב שהטור הנ“ל מגדיר בתחום ההכנסות שלו את הפונקציה $f:D\rightarrow\mathbb{R}$ ע״י $f\left(x\right)=\overset{\infty}{\underset{k=0}{\sum}}a_{k}\left(x-x_{0}\right)^{k}$ 
 נסמן** בנוסף $$
 \begin{align*} \forall x\in D\,\forall n\in\mathbb{N}\quad f_{n}\left(x\right)=\sum_{k=0}^{n}a_{k}\left(x-x_{0}\right)^{k} \end{align*} $$
 ונשים לב שמתקיים $\underset{n\rightarrow\infty}{\lim}f_{n}\left(x\right)=f\left(x\right)$ . ובנוסף $f_{n}\in\mathbb{R}\left[x\right]$ ומקיימת $\deg f_{n}\leq n$ . זהו בפרט טור פונקציות 
 
## 4 . רדיוס התכנסות 
 בהינתן $L$ (כתוצאה מקושי-הדאמאר או מדלמבר), נקרא ל $R:=\frac{1}{L}$ **רדיוס ההתכנסות של הטור $\overset{\infty}{\underset{k=0}{\sum}}a_{k}\left(x-x_{0}\right)^{k}$** , 
 כאשר מוסכם בהקשר זה $\frac{1}{0}=\infty,\frac{1}{\infty}=0$ , ומתקיים $R=\underset{x\in D}{\sup}\left|x-x_{0}\right|$ . 
 כאשר $0<R\in\mathbb{R}$ , מתקיים $\left(x_{0}-R,x_{0}+R\right)\subseteq D\subseteq\left[x_{0}-R,x_{0}+R\right]$ . 
 אזי למרות שהוגדר בעזרת קושי-הדאמר, בהינתן $D$ נוכל לחשב $R$ בעזרת $D$ . 
 
## 5 . אנליטיות 
 בהינתן $f$ , נאמר ש $f\left(x\right)$ **אנליטית ב $x_{0}$** אם“ם קיימים $0<r\in\mathbb{R}$ , וסדרה $\left(a_{k}\right)_{k=0}^{\infty}$ כך ש $$
 \begin{align*} \forall x\in\left(x_{0}-r,x_{0}+r\right)\,f\left(x\right)=\sum_{k=0}^{\infty}a_{k}\left(x-x_{0}\right)^{k} \end{align*} $$
 כלומר אם״ם **קיימת ל- $f$ הצגה כטור חזקות בסביבת $x_{0}$**. 
# משפטים 
 
## 1 . משפט קושי-הדאמר 
 תהא $\left(a_{k}\right)_{k=0}^{\infty}$ סדרה ב $\mathbb{R}$ , ו $x_{0}\in\mathbb{R}$ . 
 נסמן ב $L$ את הגבול במובן הרחב $\underset{k\rightarrow\infty}{\limsup}\sqrt[k]{\left|a_{k}\right|}$ . אזי אם: 
*  $L=0$ אזי הטור $\overset{\infty}{\underset{k=0}{\sum}}a_{k}\left(x-x_{0}\right)^{k}$ מתכנס בהחלט לכל $x\in\mathbb{R}$ 
*  $L=\infty$ אזי הטור $\overset{\infty}{\underset{k=0}{\sum}}a_{k}\left(x-x_{0}\right)^{k}$ מתבדר לכל $x\ne x_{0}$ 
*  $0<L\in\mathbb{R}$ אזי הטור $\overset{\infty}{\underset{k=0}{\sum}}a_{k}\left(x-x_{0}\right)^{k}$ מתכנס בהחלט לכל $x\in\left(x_{0}-\frac{1}{L},x_{0}+\frac{1}{L}\right)$ ומתבדר לכל $x\notin\left(x_{0}-\frac{1}{L},x_{0}+\frac{1}{L}\right)$ 
## 2 . משפט דלמבר 
 יהיו $x_{0}\in\mathbb{R}$ , $\left(a_{k}\right)_{k=0}^{\infty}$ סדרה ב $\mathbb{R}$ שונים מאפס החל ממקום מסויים, עבורה קיים הגבול במובן הרחב $\underset{k\rightarrow\infty}{\lim}\frac{\left|a_{k+1}\right|}{\left|a_{k}\right|}=L$ 
 אזי רדיוס ההתכנסות $R$ של טור החזקות $\overset{\infty}{\underset{k=0}{\sum}}a_{k}\left(x-x_{0}\right)^{k}$ הנו $R=\frac{1}{L}$ , עם אותן ההסכמות בהגדרת $R$ . 
 
## 3 . למה-קירוב טור חזקות 
 יהי $f\left(x\right)=\overset{\infty}{\underset{k=0}{\sum}}a_{k}\left(x-x_{0}\right)^{k}$ טור חזקות בעל רדיוס התכנסות $R>0$ ויהי $r\in\left(0,R\right)$ . אזי מתקיים $$
 \begin{align*} \forall\varepsilon>0\,\exists N\in\mathbb{N}\,\forall x\in\left[x_{0}-r,x_{0}+r\right]\,\forall n\geq N\quad\left|f\left(x\right)-f_{n}\left(x\right)\right|\leq\varepsilon \end{align*} $$
## 4 . רציפות טור חזקות 
 יהי $f\left(x\right)=\overset{\infty}{\underset{k=0}{\sum}}a_{k}\left(x-x_{0}\right)^{k}$ טור חזקות בעל רדיוס התכנסות $0<R\in\mathbb{R}$ . אזי הפונקציה $f$ רציפה ב $\left(x_{0}-R,x_{0}+R\right)$ 
 
## 5 . למה: $\underset{n\rightarrow\infty}{\limsup}\sqrt[n]{\left|a_{n}\right|}=\underset{n\rightarrow\infty}{\limsup}\sqrt[n+1]{\left|a_{n}\right|}$ 
 בהינתן הסדרה $\left(a_{n}\right)_{n=0}^{\infty}$ , מתקיים $\underset{n\rightarrow\infty}{\limsup}\sqrt[n]{\left|a_{n}\right|}=\underset{n\rightarrow\infty}{\limsup}\sqrt[n+1]{\left|a_{n}\right|}$ . 
 
### 6 . לטור חזקות רדיוס התכנסות זהה לטור הנגזר ממנו 
כלומר לטורים $$
 \begin{align*} \sum_{n=0}^{\infty}\frac{a_{n-1}}{n}\left(x-x_{0}\right)^{n}=\sum_{n=0}^{\infty}\frac{a_{n}}{n+1}\left(x-x_{0}\right)^{n+1},\sum_{n=0}^{\infty}a_{n}\left(x-x_{0}\right)^{n} \end{align*} $$
 אותו __רדיוס__ התכנסות 
 הערה: לא חייב להיות להם אותו __תחום__ התכנסות 
 **מסקנה** בשילוב עם המשפט על אינטגרציה איבר איבר, נקבל שבנוסף הטורים חולקים את רדיוס ההתכנסות עם הטור $$
 \begin{align*} \sum_{n=0}^{\infty}na_{n}\left(x-x_{0}\right)^{n-1}=\sum_{n=0}^{\infty}\left(n+1\right)a_{n}\left(x-x_{0}\right)^{n} \end{align*} $$
 
 **הבהרה** רדיוס ההתנסות של פונקציה המוגדרת כנ“ל זהה גם לרדיוס ההתכנסות של הנגזרת וגם של הפונקציה הקדומה שלו! 
## 7 . אינטגרציה איבר-איבר של טורי חזקות 
 יהי $f\left(x\right)=\stackrel[n=0]{\infty}{\sum}a_{n}\left(x-x_{0}\right)^{k}$ טור חזקות בעל רדיוס התכנסות $0<R$ . אזי מתקיים לכל $x\in\left(x_{0}-R,x_{0}+R\right)$ : 
 $$
 \begin{align*} \int_{x_{0}}^{x}f\left(t\right)dt=\int_{x_{0}}^{x}\left(\sum_{n=0}^{\infty}a_{n}\left(t-x_{0}\right)^{n}\right)dt=\sum_{n=0}^{\infty}\int_{x_{0}}^{x}a_{n}\left(t-x_{0}\right)^{n}dt=\sum_{n=0}^{\infty}\frac{a_{n}}{n+1}\left(t-x_{0}\right)^{n+1} \end{align*} $$
 
 מסקנה הפונקציה $\sum_{n=0}^{\infty}\frac{a_{n}}{n+1}\left(t-x_{0}\right)^{n+1}$ היא פונקציה קדומה של $\overset{\infty}{\underset{n=0}{\sum}}a_{n}\left(x-x_{0}\right)^{n}$ 
 
## 8 . גזירה איבר איבר של טורי חזקות 
 יהי $f\left(x\right)=\overset{\infty}{\underset{n=0}{\sum}}a_{n}\left(x-x_{0}\right)^{n}$ טור חזקות בעל רדיוס התכנסות $0<R$ . אזי $f$ גזירה בכל $x\in\left(x_{0}-R,x_{0}+R\right)$ ומתקיים $$
 \begin{align*} f'\left(x\right)=\sum_{n=0}^{\infty}\left(n+1\right)a_{n}\left(x-x_{0}\right)^{n} \end{align*} $$
 
 הוכחה בעזרת המשפט על אינטגרציה איבר איבר 
 
### מסקנה 
 כל נגזרת מכל סדר ניתנת להצגה כטור חזקות 
 
## 9 . יחידות טור חזקות המייצג פונקציה 
 תהי $f$ פונקציה בעלת נגזרת מכל סדר ב $x_{0}\in\mathbb{R}$ . אם יש ל- $f$ יצוג כטור חזקות בסביבה כלשהי של $x_{0}$ , הוא יחיד, ומתקיים $\forall k\in\mathbb{N}\cup\left\{ 0\right\} \quad a_{k}=\frac{f^{\left(k\right)}\left(x_{0}\right)}{k!}$ 
 
## 10 . ל- $f$ קיימת הצגה כטור חזקות אם״ם $f$ היא הגבול של $\left(P_{m,f,x_{0}}\right)_{m=1}^{\infty}$ 
 הוכחה לפי המשפט על יחידות הייצוג של טור חזקות, ובנוסף אפשר להוכיח עם יחידות פולינום טיילור ולהשאיף לאינסוף. 
 
## 11 . ל- $f$ קיימת הצגה כטור חזקות אם“ם $\underset{m\rightarrow\infty}{\lim}R_{m,f,x_{0}}\left(x\right)=0$ 
 נובע מההוכחה הקודמת, בנוסף למשפט על שארית הפיתוח של פולינומי טיילור 
 
## 12 . הלמה של אבל $\left(\text{Abel}\right)$ 
 תהי $\mathbb{R}\supseteq\left(a_{k}\right)_{k=0}^{\infty}$ סדרה נתונה. 
 
### המקרה הפרטי 
 אם קיים $0\ne x_{1}\in\mathbb{R}$ שעבורו הטור $\overset{\infty}{\underset{k=0}{\sum}}a_{k}x_{1}^{k}$ , אזי הטור $\overset{\infty}{\underset{k=0}{\sum}}a_{k}x^{k}$ מתכנס לכל $x\in\mathbb{R}$ המקיים $\left|x\right|<\left|x_{1}\right|$ . 
 
### המקרה הכללי: 
 אם קיים $x_{0}\ne x_{1}$ עבורו הטור $\overset{\infty}{\underset{k=0}{\sum}}a_{k}\left(x_{1}-x_{0}\right)^{k}$ מתכנס, אזי הטור $\overset{\infty}{\underset{k=0}{\sum}}a_{k}\left(x-x_{0}\right)^{k}$ מתכנס להחלט לכל $x\in\mathbb{R}$ המקיים $\left|x-x_{0}\right|<\left|x-x_{1}\right|$ . 
