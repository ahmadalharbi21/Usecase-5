import streamlit as st

def main():
    st.title("رحلة أحمد في البحث عن وظيفة")

    st.write("""
     قرر احمد أن يبدأ رحلة البحث عن وظيفة تناسب طموحاته. 
    في طريقه، اكتشف أحمد بعض الحقائق التي ساعدته في اتخاذ قراره:
    1. توزيع فرص العمل عبر مناطق المملكة.
    2. كيف تُعرض إعلانات الوظائف للجنسين.
    3. الرواتب المتوقعة للخريجين الجدد.
    4. مقارنة فرص العمل بين الخريجين الجدد وذوي الخبرة.
    """)

    # الجزء الأول: فرص العمل عبر المناطق
    st.subheader("الجزء الأول: فرص العمل عبر مناطق المملكة")
    st.image("jobs.png", caption="خريطة توزيع الوظائف حسب المنطقة")
    st.write("""
    أثناء بحثه، لاحظ أحمد أن بعض المناطق تزخر بفرص العمل أكثر من غيرها. 
    هذا الاكتشاف دفعه للتفكير في الانتقال إلى إحدى هذه المناطق لزيادة فرصه في الحصول على وظيفة.
    """)

    # الجزء الثاني: إعلانات الوظائف وتوزيع الجنس
    st.subheader("الجزء الثاني: فهم أحمد لتوزيع إعلانات الوظائف بين الجنسين")
    st.image("gender.png", caption="توزيع الجنس في إعلانات الوظائف")
    st.write("""
    في مرحلة لاحقة، اكتشف أحمد أن بعض الشركات تحرص على تنوع فرق العمل بين الجنسين. 
    هذه المعلومات ساعدته على تقييم كيفية تقديم نفسه بشكل أفضل لتناسب احتياجات السوق.
    """)

    # الجزء الثالث: توقعات الرواتب للخريجين الجدد
    st.subheader("الجزء الثالث: توقعات الرواتب وآمال أحمد")
    st.image("graduate.png", caption="توقعات الرواتب للخريجين الجدد")
    st.write("""
    بحث أحمد عن نطاق الرواتب المتوقعة للخريجين، فوجد أن الأرقام تتراوح بين الحد الأدنى والحد الأعلى. 
    هذا الأمر عزز ثقته وأعطاه فكرة واضحة عن الدخل الذي يمكنه تحقيقه عند بدء مسيرته المهنية.
    """)

    # الجزء الرابع: فرص العمل: الخريجين مقابل ذوي الخبرة
    st.subheader("الجزء الرابع: التحدي بين المبتدئين وذوي الخبرة")
    st.image("exper.png", caption="مقارنة فرص العمل بين الخريجين وذوي الخبرة")
    st.write("""
    أخيرًا، واجه أحمد واقع السوق الذي يفرق بين فرص العمل المخصصة للخريجين الجدد وتلك التي تتطلب خبرة. 
    هذا التحدي جعله يدرك أهمية اكتساب الخبرات التدريجية لتحسين فرصه المستقبلية.
    """)

    st.write("""
    وهكذا، بدأت رحلة أحمد مع معلومات قيمة حول سوق العمل. 
    يبقى السؤال: هل ستثمر جهوده عن تحقيق أحلامه؟ فقط الزمن سيكشف له ذلك.
    """)

if __name__ == "__main__":
    main()
