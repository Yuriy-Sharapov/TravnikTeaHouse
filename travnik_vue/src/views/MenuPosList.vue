<template>
    <div>
        <div class="col mb-4" :key="menupos.id">
            <div class="card h-100">
                <img src={{menupos.get_image_url}} class="card-img-top" alt="...">
                <div class="card-body">
                    <h5 class="card-title">{{ menupos.name }}</h5>
                    <p class="card-text">{{ menupos.descr }}</p>
                </div>
            </div>
        </div>
    </div>
</template>

<script>
    // @ is an alias to /src
    import axios from 'axios'
    export default {
        name: 'menupos-list',
        data(){
            return {
                menupos_list:[]
            }
        },
        mount(){
            this.getList()
        },
        methods:{
            getList(){
                //axios.get('menucategory/<int\:category_id>/').then( response => this.menupos_list=response.data))
                axios.get('menucategory').then(response => this.menupos_list=response.data)
            }
        }
    }
</script>