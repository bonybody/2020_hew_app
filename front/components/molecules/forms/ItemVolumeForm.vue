<template>
  <div class="form-parts">
    <div class="form-parts__heading">
      <div class="form-parts__label">
        <app-form-label :name="'volume'">1セットあたりの内容量</app-form-label>
      </div>
      <div class="form-parts__require">
        <app-require-mark v-show="require"/>
      </div>
    </div>
    <div class="form-parts__input">
      <app-input-text
          :type="'text'"
          :name="'volume'"
          :placeholder="'例：10kg'"
          v-model="inputValue"
      />
    </div>
    <div class="form-parts__error">
      <app-error-message>{{ error }}</app-error-message>
    </div>
  </div>
</template>

<script>
import AppFormLabel from "~/components/atoms/forms/label/AppFormLabel";
import AppRequireMark from "~/components/atoms/forms/marks/AppRequireMark";
import AppInputText from "~/components/atoms/forms/input/AppInputText";
import input from "~/mixins/input";
import AppErrorMessage from "~/components/atoms/forms/error/AppErrorMessage";

export default {
  name: "ItemVolumeForm",
  components: {AppErrorMessage, AppInputText, AppRequireMark, AppFormLabel},
  mixins: [input],
  props: {
    error: {
      type: String,
      require: true
    },
    require: {
      type: Boolean,
      require: true
    }
  }
}
</script>

<style scoped lang="scss">
.form-parts {
  @include form-section-mixin;

  &__heading {
    @include left-right-alignment-mixin;
  }
}
</style>