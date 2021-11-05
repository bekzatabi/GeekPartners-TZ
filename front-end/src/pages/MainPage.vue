<template>
    <div class="main">
        <div class="main__title">
            Добро пожаловать!
        </div>
        <div class="main__link">
            Перейти к <router-link to="/orders"><span>заказам</span></router-link>
        </div>
    </div>
</template>

<script>
export default {
    
}
</script>

<style scoped>
    .main{
        display: block;
    }
    .main .main__title{
        font-size: 40px;
        font-weight: bold;
    }
    .main .main__link{
        font-size: 30px;
        font-weight: 500;

    }
     .main .main__link span{
         color: red;
         text-decoration: underline;
         cursor: pointer;
     }
</style>