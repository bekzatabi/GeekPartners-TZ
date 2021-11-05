<template>
    <div class="order">
        <div>
            {{ order.number }}
        </div>
        <div v-for="product in order.data_order"
        :key="product.id" 
        class="product">
            <div>
                name: {{product.product}}
            </div>
            <div>
             amount: {{product.amount}}
            </div>
        </div>
        <div>
            status: {{ order.status.name }}
        </div>
    </div>
</template>

<script>
import axios from '../config/axios';
export default {
    data(){
        return{
            order: {}
        }
    },
    beforeMount(){
        axios.get(`/order_detail/${this.$route.params.orderId }`).then(res=>{
            this.order = res.data
        })
    }
}
</script>

<style scoped>
    .order{
        box-shadow: 0 0 5px 8px #ccc;
    }
    .product{
        margin-top: 5px;
        border: 1px solid red;
    }
</style>