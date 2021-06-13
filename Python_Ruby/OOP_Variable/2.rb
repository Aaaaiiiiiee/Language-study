class C
    def initialize(value)
        @value = value
    end

    def setValue(value)
        @value = value
    end

    def getValue()
        return @value
    end
    
    def show()
        p @value
    end
end

c1 = C.new(10)
c1.show()

c1.setValue(20)
p c1.getValue()