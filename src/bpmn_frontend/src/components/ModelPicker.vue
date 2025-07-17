<template>
  <v-select
    class="model-picker"
    placeholder="Select model"
    density="compact"
    :items="availableModels"
    :modelValue="selectedModel"
    @update:modelValue="onModelChange"
    hide-details
    :list-props="{ density: 'compact' }"
    no-data-text="Please provide API keys"
    variant="outlined"
  ></v-select>
</template>

<script>
const Models = Object.freeze({
  GPT_4_1_MINI: 'gpt-4.1-mini',
  GPT_4_1: 'gpt-4.1',
  O4_MINI: 'o4-mini',
  SONNET_4: 'claude-sonnet-4-20250514',
  OPUS_4: 'claude-opus-4-20250514',
  GEMINI_2_5_PRO: 'gemini/gemini-2.5-pro-preview-03-25',
  GEMINI_2_5_FLASH: 'gemini/gemini-2.5-flash-preview-04-17',
  LLAMA_4_MAVERICK:
    'fireworks_ai/accounts/fireworks/models/llama4-maverick-instruct-basic',
  QWEN_3_235B: 'fireworks_ai/accounts/fireworks/models/qwen3-235b-a22b',
  DEEPSEEK_V3: 'fireworks_ai/accounts/fireworks/models/deepseek-v3',
  DEEPSEEK_R1: 'fireworks_ai/accounts/fireworks/models/deepseek-r1',
});

const Providers = Object.freeze({
  OPENAI: 'openai',
  ANTHROPIC: 'anthropic',
  GOOGLE: 'google',
  FIREWORKS_AI: 'fireworks_ai',
});

export default {
  name: 'ModelPicker',
  data() {
    return {
      selectedModel: '',
      models: [
        { value: Models.GPT_4_1, title: 'GPT-4.1', provider: Providers.OPENAI },
        {
          value: Models.GPT_4_1_MINI,
          title: 'GPT-4.1 mini',
          provider: Providers.OPENAI,
        },
        {
          value: Models.O4_MINI,
          title: 'o4-mini',
          provider: Providers.OPENAI,
        },
        {
          value: Models.SONNET_4,
          title: 'Claude Sonnet 4',
          provider: Providers.ANTHROPIC,
        },
        {
          value: Models.OPUS_4,
          title: 'Claude Opus 4',
          provider: Providers.ANTHROPIC,
        },
        {
          value: Models.GEMINI_2_5_FLASH,
          title: 'Gemini 2.5 Flash',
          provider: Providers.GOOGLE,
        },
        {
          value: Models.GEMINI_2_5_PRO,
          title: 'Gemini 2.5 Pro',
          provider: Providers.GOOGLE,
        },
        {
          value: Models.LLAMA_4_MAVERICK,
          title: 'Llama 4 Maverick',
          provider: Providers.FIREWORKS_AI,
        },
        {
          value: Models.QWEN_3_235B,
          title: 'Qwen 3',
          provider: Providers.FIREWORKS_AI,
        },
        {
          value: Models.DEEPSEEK_V3,
          title: 'Deepseek V3',
          provider: Providers.FIREWORKS_AI,
        },
        {
          value: Models.DEEPSEEK_R1,
          title: 'Deepseek R1',
          provider: Providers.FIREWORKS_AI,
        },
      ],
      availableProviders: [],
    };
  },
  computed: {
    availableModels() {
      return this.models.filter((model) =>
        this.availableProviders.includes(model.provider)
      );
    },
  },
  methods: {
    onModelChange(model) {
      this.selectedModel = model;
      this.$emit('select-model', model);
    },
    async fetchAvailableProviders() {
      try {
        const response = await fetch(
          'https://bpm-assistant.cloud.anjokolk.com/available_providers',
          {
            method: 'GET',
            headers: { 'Content-Type': 'application/json' },
          }
        );

        if (!response.ok) {
          throw new Error(`HTTP error! status: ${response.status}`);
        }

        const data = await response.json();

        this.availableProviders = Object.keys(data).filter(
          (provider) => data[provider]
        );

        if (this.availableProviders.includes(Providers.OPENAI)) {
          this.onModelChange(Models.GPT_4_1);
        } else if (this.availableProviders.includes(Providers.ANTHROPIC)) {
          this.onModelChange(Models.SONNET_4);
        } else if (this.availableProviders.includes(Providers.GOOGLE)) {
          this.onModelChange(Models.GEMINI_2_5_PRO);
        } else if (this.availableProviders.includes(Providers.FIREWORKS_AI)) {
          this.onModelChange(Models.LLAMA_4_MAVERICK);
        }
      } catch (error) {
        console.error('Error fetching available providers', error);
      }
    },
  },
  mounted() {
    this.fetchAvailableProviders();
  },
};
</script>

<style scoped>
.model-picker {
  width: 200px;
}
</style>
