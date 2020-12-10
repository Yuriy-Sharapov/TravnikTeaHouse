<template>
    <!--    Меню-->
    <div class="container sTopline">
        <b-navbar toggleable="lg" type="dark" variant="info">
            <b-nav-item-dropdown text="Меню" left v-for="menucategory in menucategory_list" :key="menucategory.id">
                <b-dropdown-item href="#">{{menucategory.name}}</b-dropdown-item>
            </b-nav-item-dropdown>

            <b-navbar-nav>
                <b-nav-item href="#">Угадаем настроение</b-nav-item>
                <b-nav-item href="#">О нас</b-nav-item>
                <b-nav-item href="#">Контакты</b-nav-item>
            </b-navbar-nav>

            <b-navbar-nav class="ml-auto">
                <b-navbar-nav>
                    <b-nav-item href="#">Корзина</b-nav-item>
                    <b-nav-item href="#">Вход</b-nav-item>
                </b-navbar-nav>
            </b-navbar-nav>
        </b-navbar>
    </div>
</template>

<script>
    import axios from 'axios'

    export default {
        name: "MyNavBar",
        data(){
            return {
                menucategory_list:[]
            }
        },
        mounted() {
            this.getList()
        },
        methods:{
            getList(){
                axios.get('menucategory').then(response => this.menucategory_list = response.data)
            }
        }
    }
</script>

<style scoped>

</style>