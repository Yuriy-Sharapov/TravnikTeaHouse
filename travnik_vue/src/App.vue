<template>
  <div id="app">
    <div id="nav">
      <!--    Надменю-->
      <div class="container sUpTopline">
        <nav class="navbar navbar-expand-lg navbar-light">
          <a class="navbar-brand" href="/tthapp/">
            <img src="#/static/image/cap2.png" class="sLogo">
          </a>
          <button class="navbar-toggler" type="button" data-toggle="collapse" data-target="#navbarSupportedContent" aria-controls="navbarSupportedContent" aria-expanded="false" aria-label="Toggle navigation">
            <span class="navbar-toggler-icon"></span>
          </button>

          <div class="collapse navbar-collapse" id="navbarSupportedContent">
            <ul class="navbar-nav mr-auto">
              <li class="nav-item">
                <div>
                  <svg width="1em" height="1em" viewBox="0 0 16 16" class="bi bi-geo-alt" fill="currentColor" xmlns="http://www.w3.org/2000/svg" >
                    <path fill-rule="evenodd" d="M12.166 8.94C12.696 7.867 13 6.862 13 6A5 5 0 0 0 3 6c0 .862.305 1.867.834 2.94.524 1.062 1.234 2.12 1.96 3.07A31.481 31.481 0 0 0 8 14.58l.208-.22a31.493 31.493 0 0 0 1.998-2.35c.726-.95 1.436-2.008 1.96-3.07zM8 16s6-5.686 6-10A6 6 0 0 0 2 6c0 4.314 6 10 6 10z"/>
                    <path fill-rule="evenodd" d="M8 8a2 2 0 1 0 0-4 2 2 0 0 0 0 4zm0 1a3 3 0 1 0 0-6 3 3 0 0 0 0 6z"/>
                  </svg>
                  <a class="nav-link" href="#">Пермь, ул. Энгельса, 18</a>
                </div>
              </li>
              <li class="nav-item">
                <div>
                  <svg width="1em" height="1em" viewBox="0 0 16 16" class="bi bi-telephone" fill="currentColor" xmlns="http://www.w3.org/2000/svg">
                    <path fill-rule="evenodd" d="M3.654 1.328a.678.678 0 0 0-1.015-.063L1.605 2.3c-.483.484-.661 1.169-.45 1.77a17.568 17.568 0 0 0 4.168 6.608 17.569 17.569 0 0 0 6.608 4.168c.601.211 1.286.033 1.77-.45l1.034-1.034a.678.678 0 0 0-.063-1.015l-2.307-1.794a.678.678 0 0 0-.58-.122l-2.19.547a1.745 1.745 0 0 1-1.657-.459L5.482 8.062a1.745 1.745 0 0 1-.46-1.657l.548-2.19a.678.678 0 0 0-.122-.58L3.654 1.328zM1.884.511a1.745 1.745 0 0 1 2.612.163L6.29 2.98c.329.423.445.974.315 1.494l-.547 2.19a.678.678 0 0 0 .178.643l2.457 2.457a.678.678 0 0 0 .644.178l2.189-.547a1.745 1.745 0 0 1 1.494.315l2.306 1.794c.829.645.905 1.87.163 2.611l-1.034 1.034c-.74.74-1.846 1.065-2.877.702a18.634 18.634 0 0 1-7.01-4.42 18.634 18.634 0 0 1-4.42-7.009c-.362-1.03-.037-2.137.703-2.877L1.885.511z"/>
                  </svg>
                  <a class="nav-link" href="#">8 (904) 324-23-52</a>
                </div>
              </li>
            </ul>
            <form class="form-inline my-2 my-lg-0">
              <input class="form-control sSearshField" type="search" placeholder="Найти" aria-label="Search">
              <button class="btn btn-outline-success my-2 my-sm-0 sSearshButton" type="submit">
                <!--                            Иконка лупы-->
                <svg width="1em" height="1em" viewBox="0 0 16 16" class="bi bi-search" fill="currentColor" xmlns="http://www.w3.org/2000/svg">
                  <path fill-rule="evenodd" d="M10.442 10.442a1 1 0 0 1 1.415 0l3.85 3.85a1 1 0 0 1-1.414 1.415l-3.85-3.85a1 1 0 0 1 0-1.415z"/>
                  <path fill-rule="evenodd" d="M6.5 12a5.5 5.5 0 1 0 0-11 5.5 5.5 0 0 0 0 11zM13 6.5a6.5 6.5 0 1 1-13 0 6.5 6.5 0 0 1 13 0z"/>
                </svg>
              </button>
            </form>
          </div>
        </nav>
      </div>

      <MyNavBar></MyNavBar>
<!--      &lt;!&ndash;    Меню&ndash;&gt;-->
<!--      <div class="container sTopline">-->
<!--        <b-navbar toggleable="lg" type="dark" variant="info">-->
<!--&lt;!&ndash;          <b-navbar-brand href="#">Меню</b-navbar-brand>&ndash;&gt;-->
<!--          <b-nav-item-dropdown text="Меню">-->
<!--            <b-dropdown-item href="#">EN</b-dropdown-item>-->
<!--            <b-dropdown-item href="#">ES</b-dropdown-item>-->
<!--            <b-dropdown-item href="#">RU</b-dropdown-item>-->
<!--            <b-dropdown-item href="#">FA</b-dropdown-item>-->
<!--          </b-nav-item-dropdown>-->

<!--&lt;!&ndash;          <b-navbar-toggle target="nav-collapse"></b-navbar-toggle>&ndash;&gt;-->

<!--&lt;!&ndash;          <b-collapse id="nav-collapse" is-nav>&ndash;&gt;-->
<!--            <b-navbar-nav>-->
<!--              <b-nav-item href="#">Угадаем настроение</b-nav-item>-->
<!--              <b-nav-item href="#">О нас</b-nav-item>-->
<!--              <b-nav-item href="#">Контакты</b-nav-item>-->
<!--            </b-navbar-nav>-->

<!--            &lt;!&ndash; Right aligned nav items &ndash;&gt;-->
<!--          <b-navbar-nav class="ml-auto">-->
<!--            <b-navbar-nav>-->
<!--              <b-nav-item href="#">Корзина</b-nav-item>-->
<!--              <b-nav-item href="#">Вход</b-nav-item>-->
<!--            </b-navbar-nav>-->
<!--          </b-navbar-nav>-->
<!--&lt;!&ndash;          </b-collapse>&ndash;&gt;-->
<!--        </b-navbar>-->
<!--      </div>-->

<!--      <div class="container sTopline">-->
<!--        <nav class="navbar navbar-expand-lg navbar-light">-->
<!--          <div class="collapse navbar-collapse" id="navbarSupportedContent">-->
<!--            <ul class="navbar-nav mr-auto">-->
<!--&lt;!&ndash;              <b-nav-item-dropdown text="Меню" right>&ndash;&gt;-->
<!--&lt;!&ndash;                <b-dropdown-item href="#">Десерты</b-dropdown-item>&ndash;&gt;-->
<!--&lt;!&ndash;                <b-dropdown-item href="#">Десерты</b-dropdown-item>&ndash;&gt;-->
<!--&lt;!&ndash;                <b-dropdown-item href="#">RU</b-dropdown-item>&ndash;&gt;-->
<!--&lt;!&ndash;                <b-dropdown-item href="#">FA</b-dropdown-item>&ndash;&gt;-->
<!--&lt;!&ndash;              </b-nav-item-dropdown>&ndash;&gt;-->

<!--              <li class="nav-item active dropdown">-->
<!--                <router-link class="nav-link dropdown-toggle" to="#" id="navbarDropdown" role="button" data-toggle="dropdown" aria-haspopup="true" aria-expanded="false">-->
<!--                  Меню-->
<!--                </router-link>-->
<!--                <div class="dropdown-menu" aria-labelledby="navbarDropdown">-->
<!--                  <router-link class="dropdown-item" to="#">Десерты</router-link>-->
<!--                  <router-link class="dropdown-item" to="#">Десерты</router-link>-->
<!--                  <router-link class="dropdown-item" to="#">Десерты</router-link>-->
<!--                  <router-link class="dropdown-item" to="#">Десерты</router-link>-->
<!--&lt;!&ndash;                  {% for menucategory in menucategory_list  %}&ndash;&gt;-->
<!--&lt;!&ndash;                  <router-link class="dropdown-item" href="{% url 'menucategory' menucategory.id %}">{{menucategory.name}}</router-link>&ndash;&gt;-->
<!--&lt;!&ndash;                  {% endfor %}&ndash;&gt;-->
<!--                </div>-->
<!--              </li>-->
<!--              <li class="nav-item">-->
<!--                <router-link class="nav-link" to="#">Угадаем настроение <span class="sr-only">(current)</span></router-link>-->
<!--              </li>-->
<!--              <li class="nav-item">-->
<!--                <router-link class="nav-link" to="#">О нас</router-link>-->
<!--              </li>-->
<!--              <li class="nav-item">-->
<!--                <router-link class="nav-link" to="#">Контакты</router-link>-->
<!--              </li>-->
<!--              <li class="nav-item">-->
<!--                <router-link class="nav-link" to="#">Корзина</router-link>-->
<!--              </li>-->
<!--              <li class="nav-item">-->
<!--                <router-link class="nav-link" to="#">Вход</router-link>-->
<!--              </li>-->
<!--            </ul>-->
<!--          </div>-->
<!--        </nav>-->
<!--      </div>-->
<!--      <router-link to="/">Home</router-link> |-->
<!--      <router-link to="/about">About</router-link>-->
    </div>
    <div class="container">
      <router-view/>
    </div>
  </div>
</template>

<style lang="scss">

</style>
